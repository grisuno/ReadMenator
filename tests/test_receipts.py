import json
import os
from pathlib import Path

import pytest

from readmenator._hypotheses import (
    STATUS_VERIFIED,
    Hypothesis,
    HypothesisValidator,
)
from readmenator._receipts import (
    KIND_CANDIDATE,
    KIND_PREDICTED,
    EdgeInfo,
    ReceiptIngestor,
    ReceiptsReconciler,
    ReleaseReceiptRecord,
)
from readmenator._uncertainty import (
    FEATURE_NAMES,
    HeuristicScorer,
    featurize,
    predict_uncertain_edges,
    prediction_edges,
)

RECEIPT_A = {
    "schema": "deploynator/receipt@v1",
    "mode": "run",
    "status": "failed",
    "project": "p1",
    "dry_run": False,
    "trace": False,
    "flags": {},
    "version_from": "1.2.3",
    "version_to": "1.2.4",
    "tag": "1.2.4",
    "commit": "abc",
    "branch": "main",
    "error": "Some platforms failed",
    "steps": [
        {"step": "commit", "status": "ok"},
        {"step": "tag", "status": "ok"},
        {"step": "push:origin", "status": "failed", "error": "denied"},
    ],
    "commands": [
        {"command": ["git", "-C", "/x", "tag", "-a", "1.2.4", "-m", "v"],
         "exit_code": 0, "success": True, "stage": "tag", "kind": "observed",
         "cwd": "", "stdout_tail": "", "stderr_tail": "", "exception": ""},
        {"command": ["git", "-C", "/x", "push", "origin", "main"],
         "exit_code": 128, "success": False, "stage": "push:origin",
         "kind": "observed", "cwd": "", "stdout_tail": "", "stderr_tail": "",
         "exception": ""},
        {"command": ["gh", "release", "create", "1.2.4"],
         "exit_code": 1, "success": False, "stage": "gh_release",
         "kind": "observed", "cwd": "", "stdout_tail": "", "stderr_tail": "",
         "exception": ""},
    ],
    "edges": [
        {"caller": "DeployOrchestrator.deploy", "callee": "GitOperations.tag",
         "kind": "observed", "evidence": "tag:1.2.4", "confidence": 1.0,
         "provenance": "receipt:1.2.4"},
        {"caller": "DeployOrchestrator.deploy", "callee": "GitOperations.commit",
         "kind": "observed", "evidence": "commit:abc", "confidence": 1.0,
         "provenance": "receipt:1.2.4"},
    ],
    "platforms": [{"platform": "github", "repo": "u/p1", "enabled": True,
                   "pushed": False, "released": False, "error": "push failed"}],
}

RECEIPT_B = {
    "schema": "deploynator/receipt@v1",
    "mode": "plan",
    "status": "success",
    "project": "p1",
    "dry_run": True,
    "trace": True,
    "flags": {},
    "version_from": "1.2.4",
    "version_to": "1.2.5",
    "tag": "",
    "commit": "",
    "branch": "",
    "error": "",
    "steps": [],
    "commands": [{"command": ["gitlab-cli", "release", "create", "1.2.5"],
                  "exit_code": None, "success": None, "stage": "release:gitlab",
                  "kind": "candidate", "cwd": "", "stdout_tail": "",
                  "stderr_tail": "", "exception": ""}],
    "edges": [
        {"caller": "Platform.create_release", "callee": "GitLabCLI.create_release",
         "kind": "candidate", "evidence": "config:PlatformConfig.enabled",
         "confidence": 0.5, "provenance": "config:gitlab.com/u/p1"},
        {"caller": "Platform.create_release",
         "callee": "BitbucketCLI.create_release", "kind": "candidate",
         "evidence": "config:PlatformConfig.enabled", "confidence": 0.5,
         "provenance": "config:bitbucket.org/u/p1"},
    ],
    "platforms": [{"platform": "gitlab", "repo": "u/p1", "enabled": False}],
}

RECEIPT_C = {
    "schema": "deploynator/receipt@v1",
    "mode": "run",
    "status": "success",
    "project": "p2",
    "dry_run": False,
    "version_from": "0.2.0",
    "version_to": "0.2.1",
    "tag": "0.2.1",
    "commit": "def456",
    "branch": "main",
    "error": "",
    "steps": [{"step": "commit", "status": "ok"}, {"step": "tag", "status": "ok"},
              {"step": "push:origin", "status": "ok"}],
    "commands": [],
    "edges": [{"caller": "Platform.create_release",
               "callee": "GitLabCLI.create_release", "kind": "observed",
               "evidence": "platform:gitlab", "confidence": 1.0,
               "provenance": "receipt:0.2.1"}],
    "platforms": [{"platform": "gitlab", "repo": "u/p2", "enabled": True,
                   "pushed": True, "released": True}],
}


class TestLoading:
    def test_load_bad_schema_rejected(self, tmp_path):
        path = tmp_path / "bad.json"
        path.write_text(json.dumps({"schema": "other/tool@v9", "project": "x"}))
        with pytest.raises(ValueError):
            ReceiptIngestor().load_file(str(path))

    def test_load_valid_record(self, tmp_path):
        path = tmp_path / "a.json"
        path.write_text(json.dumps(RECEIPT_A))
        record = ReceiptIngestor().load_file(str(path))
        assert record.project == "p1"
        assert record.version_to == "1.2.4"
        assert record.platforms[0]["platform"] == "github"

    def test_load_dir_sorted_and_invalid_skipped(self, tmp_path):
        (tmp_path / "a.json").write_text(json.dumps(RECEIPT_A))
        (tmp_path / "b.json").write_text(json.dumps(RECEIPT_B))
        (tmp_path / "broken.json").write_text("{not json")
        (tmp_path / "notes.txt").write_text("ignore me")
        records = ReceiptIngestor().load_dir(str(tmp_path))
        names = [r.project for r in records]
        assert names == ["p1", "p1"]

    def test_missing_dir_returns_empty(self):
        assert ReceiptIngestor().load_dir("/definitely/no/dir") == []


class TestEdges:
    def test_observed_edges_explicit(self, tmp_path):
        records = ReceiptIngestor().load_dir(str(tmp_path))
        assert records == []
        ingestor = ReceiptIngestor()
        record = ReleaseReceiptRecord.from_dict(RECEIPT_A, "a.json")
        edges = ingestor.observed_edges([record])
        pairs = {(e.caller, e.callee) for e in edges}
        assert ("DeployOrchestrator.deploy", "GitOperations.tag") in pairs
        assert ("DeployOrchestrator.deploy", "GitOperations.commit") in pairs

    def test_command_derived_edges(self):
        record = ReleaseReceiptRecord.from_dict(RECEIPT_A, "a.json")
        edges = ReceiptIngestor().observed_edges([record])
        pairs = {(e.caller, e.callee) for e in edges}
        assert ("DeployOrchestrator.deploy", "GitOperations.push") in pairs
        assert ("DeployOrchestrator._gh_release_in_repo", "GitHubCLI.create_release") in pairs

    def test_planned_commands_not_observed(self):
        record = ReleaseReceiptRecord.from_dict(RECEIPT_B, "b.json")
        edges = ReceiptIngestor().observed_edges([record])
        assert not any(e.callee.endswith("create_release") for e in edges)

    def test_candidate_edges_partition(self):
        record_b = ReleaseReceiptRecord.from_dict(RECEIPT_B, "b.json")
        candidates = ReceiptIngestor().candidate_edges([record_b])
        callees = {e.callee for e in candidates}
        assert "GitLabCLI.create_release" in callees
        assert "BitbucketCLI.create_release" in callees
        assert all(e.kind == KIND_CANDIDATE for e in candidates)


class TestReconciler:
    def _run(self, records):
        reconciler = ReceiptsReconciler()
        observed = ReceiptIngestor().observed_edges(records)
        known = {(e.caller, e.callee) for e in observed}
        candidates = ReceiptIngestor().candidate_edges(records)
        predictions = predict_uncertain_edges(candidates, known)
        predicted = prediction_edges(predictions)
        return reconciler.reconcile(records, candidates, predicted)

    def test_confirmation_resolves_candidates(self):
        records = [ReleaseReceiptRecord.from_dict(r, f"{n}.json")
                   for n, r in (("a", RECEIPT_A), ("b", RECEIPT_B), ("c", RECEIPT_C))]
        report = self._run(records)
        confirmed = {(e["caller"], e["callee"]) for e in report["confirmed_candidates"]}
        unobserved = {(e["caller"], e["callee"]) for e in report["unobserved_candidates"]}
        assert ("Platform.create_release", "GitLabCLI.create_release") in confirmed
        assert ("Platform.create_release", "BitbucketCLI.create_release") in unobserved
        assert not any(e["kind"] == KIND_PREDICTED and e["callee"] == "BitbucketCLI.create_release"
                       for e in report["predicted_edges"])

    def test_markdown_lists_platforms_and_states(self):
        records = [ReleaseReceiptRecord.from_dict(r, f"{n}.json")
                   for n, r in (("a", RECEIPT_A), ("b", RECEIPT_B))]
        reconciler = ReceiptsReconciler()
        report = self._run(records)
        text = reconciler.releases_markdown(report)
        assert "p1 1.2.3 → 1.2.4 [failed]" in text
        assert "platform github: pushed=no, released=no" in text
        assert "platform gitlab: disabled" in text
        assert "Observed edges (facts)" in text
        assert "Unobserved candidates (feasible set, not executed)" in text

    def test_write_pages_artifacts(self, tmp_path):
        target = str(tmp_path)
        records = [ReleaseReceiptRecord.from_dict(r, f"{n}.json")
                   for n, r in (("a", RECEIPT_A), ("c", RECEIPT_C))]
        reconciler = ReceiptsReconciler()
        report = self._run(records)
        out_dir = reconciler.write_pages(report, target)
        out_dir = Path(out_dir)
        assert out_dir.is_dir()
        page = (out_dir / "RELEASES.md")
        edges_file = (out_dir / "release-edges.json")
        assert os.path.isfile(page) and os.path.isfile(edges_file)
        content = page.read_text(encoding="utf-8")
        assert "p2 0.2.0 → 0.2.1 [success]" in content
        loaded = json.loads(edges_file.read_text(encoding="utf-8"))
        assert "observed_edges" in loaded


class TestUncertainty:
    def test_feature_vector_shape(self):
        edge = EdgeInfo("Platform.create_release", "GitHubCLI.create_release",
                        KIND_CANDIDATE, "cli:--platforms", 0.9)
        features = featurize(edge, set())
        assert set(features) == set(FEATURE_NAMES)
        assert features["confidence"] == 90
        assert features["evidence_cli"] == 1

    def test_heuristic_high_for_cli_evidence(self):
        edge = EdgeInfo("Platform.create_release", "GitHubCLI.create_release",
                        KIND_CANDIDATE, "cli:--platforms", 0.9)
        score = HeuristicScorer().score(featurize(edge, set()))
        assert score > 0.5

    def test_heuristic_low_for_unobserved_generic(self):
        edge = EdgeInfo("Platform.create_release", "PyPIRunner.run",
                        KIND_CANDIDATE, "toml:pypi.enabled", 0.7)
        score = HeuristicScorer().score(featurize(edge, set()))
        assert score < 0.9

    def test_predict_labels_predicted(self):
        edge = EdgeInfo("Platform.create_release", "GitHubCLI.create_release",
                        KIND_CANDIDATE, "cli:--platforms", 0.9)
        predictions = predict_uncertain_edges([edge], set(), min_confidence=0.5)
        assert predictions and predictions[0].edge.kind == KIND_CANDIDATE
        as_edges = prediction_edges(predictions)
        assert as_edges[0].kind == KIND_PREDICTED
        assert as_edges[0].evidence.startswith("model:readmenator-uncertainty")
        assert 0.0 <= as_edges[0].confidence <= 1.0

    def test_min_confidence_filters(self):
        edge = EdgeInfo("a", "b", KIND_CANDIDATE, "interface:Platform", 1.0)
        predictions = predict_uncertain_edges([edge], set(), min_confidence=0.99)
        assert predictions == []

    def test_random_forest_fallback_and_fit(self):
        from readmenator._uncertainty import RandomForestScorer
        if not RandomForestScorer.available():
            pytest.skip("sklearn not installed")
        edge = EdgeInfo("Platform.create_release", "GitHubCLI.create_release",
                        KIND_CANDIDATE, "cli:--platforms", 0.9)
        x = [featurize(edge, set()), featurize(edge, set())]
        y = [1, 0]
        with pytest.raises(ValueError):
            RandomForestScorer().fit(x, y)  # single class -> rejected

        x = [dict(featurize(edge, set()), historically_observed=0),
             dict(featurize(edge, set()), historically_observed=0),
             dict(featurize(edge, set()), historically_observed=0),
             dict(featurize(edge, set()), historically_observed=1),
             dict(featurize(edge, set()), historically_observed=1)]
        y = [1, 1, 1, 0, 0]
        scorer = RandomForestScorer()
        scorer.fit(x, y)
        score = scorer.score(featurize(edge, set()))
        assert 0.0 <= score <= 1.0


class TestHypotheses:
    def _validator(self):
        return HypothesisValidator(
            known_edges={("DeployOrchestrator.deploy", "GitOperations.tag")},
            known_symbols={"GitHubCLI", "GitHubCLI.create_release",
                           "DeployOrchestrator.deploy", "Platform.create_release"},
        )

    def test_already_observed_verified(self):
        hypothesis = Hypothesis.from_dict({"caller": "DeployOrchestrator.deploy",
                                           "callee": "GitOperations.tag"})
        verdict = self._validator().validate(hypothesis)
        assert verdict.status == STATUS_VERIFIED

    def test_callee_known_via_class_match_verified(self):
        hypothesis = Hypothesis.from_dict({
            "caller": "DeployOrchestrator.deploy",
            "callee": "GitHubCLI.create_release",
            "rationale": "get_platform returns BitbucketCLI",
        })
        verdict = self._validator().validate(hypothesis)
        assert verdict.status == STATUS_VERIFIED
        assert verdict.assumed is False

    def test_unknown_callee_rejected(self):
        hypothesis = Hypothesis.from_dict({"caller": "DeployOrchestrator.deploy",
                                           "callee": "MagicCLI.do_black_magic"})
        verdict = self._validator().validate(hypothesis)
        assert verdict.status == "rejected"
        assert any("not found in symbol index" in r for r in verdict.reasons)

    def test_unknown_caller_rejected_by_default(self):
        hypothesis = Hypothesis.from_dict({"caller": "WhoKnows.deployer",
                                           "callee": "GitHubCLI.create_release"})
        verdict = self._validator().validate(hypothesis)
        assert verdict.status == "rejected"

    def test_unknown_caller_assumed_when_allowed(self):
        hypothesis = Hypothesis.from_dict({"caller": "WhoKnows.deployer",
                                           "callee": "GitHubCLI.create_release"})
        verdict = self._validator().validate(hypothesis, allow_assumed=True)
        assert verdict.status == STATUS_VERIFIED
        assert verdict.assumed is True

    def test_json_list_validation(self):
        raw = json.dumps([
            {"caller": "DeployOrchestrator.deploy", "callee": "GitOperations.tag"},
            {"caller": "x", "callee": "GitHubCLI.create_release"},
        ])
        verdicts = self._validator().validate_json(raw)
        statuses = [v.status for v in verdicts]
        assert STATUS_VERIFIED in statuses
        assert "rejected" in statuses

    def test_missing_fields_rejected(self):
        with pytest.raises(ValueError):
            Hypothesis.from_dict({"caller": "only-caller"})

    def test_extra_context_preserved(self):
        hypothesis = Hypothesis.from_dict({
            "caller": "a", "callee": "b", "evidence": "chat",
        })
        assert hypothesis.extra == {"evidence": "chat"}
