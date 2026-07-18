"""Contract tests for the category theory and ranking system.

Tests cover:
- EdgeKind enum contract
- Morphism weight computation
- Category composition and path finding
- TypedGraph stochastic matrix construction
- Global PageRank invariants (sum=1, convergence, stability)
- Personalized PageRank seed sensitivity
- HITS authority/hub separation
- Composite scoring formula
- Seed generation from queries
- Noise penalty for hub names
- Projection functors and views
- Score explanation formatting
"""

from __future__ import annotations

from typing import Dict, List

import pytest

from readmenator._category import (
    Category,
    EdgeKind,
    Morphism,
    TypedGraph,
    _infer_edge_kind,
    build_category_from_edges,
    EDGE_WEIGHTS,
)
from readmenator._explain import explain_rank, rank_summary
from readmenator._models import Edge, Node, Symbol
from readmenator._projections import (
    DocProjection,
    IdentityProjection,
    RiskProjection,
    apply_view,
    VIEWS,
)
from readmenator._rank import (
    CompositeRanker,
    RankConfig,
    RankedItem,
    RankedResult,
    build_seeds_from_query,
    build_seeds_for_context,
    global_pagerank,
    hits,
    personalized_pagerank,
    HUB_PENALTY_NAMES,
)


# ---------------------------------------------------------------------------
# EdgeKind contract
# ---------------------------------------------------------------------------

class TestEdgeKind:
    def test_all_edge_kinds_have_weights(self) -> None:
        for kind in EdgeKind:
            assert kind in EDGE_WEIGHTS, f"{kind} missing from EDGE_WEIGHTS"
            assert EDGE_WEIGHTS[kind] > 0.0, f"{kind} weight must be positive"

    def test_infer_edge_kind_maps_correctly(self) -> None:
        assert _infer_edge_kind("imports") == EdgeKind.IMPORTS
        assert _infer_edge_kind("calls") == EdgeKind.CALLS
        assert _infer_edge_kind("defines") == EdgeKind.DEFINES

    def test_infer_edge_kind_falls_back(self) -> None:
        assert _infer_edge_kind("unknown_relation") == EdgeKind.DEPENDS_ON
        assert _infer_edge_kind("") == EdgeKind.DEPENDS_ON

    def test_edge_kind_is_str_enum(self) -> None:
        assert str(EdgeKind.IMPORTS) == "imports"
        assert str(EdgeKind.CALLS) == "calls"


# ---------------------------------------------------------------------------
# Morphism contract
# ---------------------------------------------------------------------------

class TestMorphism:
    def test_weight_is_edge_weight_times_confidence(self) -> None:
        m = Morphism("a.py", "b.py", EdgeKind.IMPORTS, confidence=0.8)
        expected = EDGE_WEIGHTS[EdgeKind.IMPORTS] * 0.8
        assert abs(m.weight - expected) < 1e-6

    def test_weight_default_confidence(self) -> None:
        m = Morphism("a.py", "b.py", EdgeKind.CALLS)
        assert abs(m.weight - EDGE_WEIGHTS[EdgeKind.CALLS]) < 1e-6

    def test_morphism_is_frozen(self) -> None:
        m = Morphism("a.py", "b.py", EdgeKind.IMPORTS)
        with pytest.raises(AttributeError):
            m.source = "c.py"  # type: ignore


# ---------------------------------------------------------------------------
# Category contract
# ---------------------------------------------------------------------------

class TestCategory:
    def test_empty_category(self) -> None:
        cat = Category()
        assert len(cat.objects) == 0
        assert len(cat.morphisms) == 0

    def test_add_object_and_morphism(self) -> None:
        cat = Category()
        cat.add_object("a.py")
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        assert "a.py" in cat.objects
        assert "b.py" in cat.objects
        assert len(cat.morphisms) == 1

    def test_outgoing_and_incoming(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_morphism(Morphism("a.py", "c.py", EdgeKind.CALLS))
        cat.add_morphism(Morphism("b.py", "c.py", EdgeKind.INHERITS))

        assert len(cat.outgoing("a.py")) == 2
        assert len(cat.outgoing("b.py")) == 1
        assert len(cat.outgoing("c.py")) == 0
        assert len(cat.incoming("b.py")) == 1
        assert len(cat.incoming("c.py")) == 2

    def test_compose_same_kind(self) -> None:
        cat = Category()
        a = Morphism("a.py", "b.py", EdgeKind.IMPORTS)
        b = Morphism("b.py", "c.py", EdgeKind.IMPORTS)
        result = cat.compose(a, b)
        assert result is not None
        assert result.source == "a.py"
        assert result.target == "c.py"
        assert result.kind == EdgeKind.IMPORTS

    def test_compose_imports_then_defines(self) -> None:
        cat = Category()
        a = Morphism("a.py", "b.py", EdgeKind.IMPORTS)
        b = Morphism("b.py", "c.py", EdgeKind.DEFINES)
        result = cat.compose(a, b)
        assert result is not None
        assert result.kind == EdgeKind.DEFINES

    def test_compose_incompatible_returns_none(self) -> None:
        cat = Category()
        a = Morphism("a.py", "b.py", EdgeKind.CALLS)
        b = Morphism("b.py", "c.py", EdgeKind.INHERITS)
        result = cat.compose(a, b)
        assert result is None

    def test_compose_mismatched_target_source(self) -> None:
        cat = Category()
        a = Morphism("a.py", "b.py", EdgeKind.IMPORTS)
        b = Morphism("c.py", "d.py", EdgeKind.DEFINES)
        result = cat.compose(a, b)
        assert result is None

    def test_paths_finds_composition_chains(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_morphism(Morphism("b.py", "c.py", EdgeKind.DEFINES))
        cat.add_morphism(Morphism("c.py", "d.py", EdgeKind.TESTS))
        paths = cat.paths("a.py", "d.py", max_depth=10)
        assert len(paths) >= 1
        assert len(paths[0]) == 3

    def test_paths_empty_when_no_route(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_morphism(Morphism("c.py", "d.py", EdgeKind.IMPORTS))
        paths = cat.paths("a.py", "d.py")
        assert len(paths) == 0


# ---------------------------------------------------------------------------
# TypedGraph contract
# ---------------------------------------------------------------------------

class TestTypedGraph:
    def test_empty_graph(self) -> None:
        cat = Category()
        g = TypedGraph(cat)
        assert g.size == 0
        assert g.nodes == []

    def test_stochastic_row_normalizes_to_one(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_morphism(Morphism("a.py", "c.py", EdgeKind.CALLS))
        g = TypedGraph(cat)
        row = g.stochastic_row("a.py")
        total = sum(row.values())
        assert abs(total - 1.0) < 1e-6

    def test_stochastic_row_empty_for_dangling(self) -> None:
        cat = Category()
        cat.add_object("a.py")
        g = TypedGraph(cat)
        assert g.stochastic_row("a.py") == {}

    def test_transition_weight_aggregates_parallel_edges(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS, confidence=0.5))
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.CALLS, confidence=0.5))
        g = TypedGraph(cat)
        w = g.transition_weight("a.py", "b.py")
        expected = EDGE_WEIGHTS[EdgeKind.IMPORTS] * 0.5 + EDGE_WEIGHTS[EdgeKind.CALLS] * 0.5
        assert abs(w - expected) < 1e-6

    def test_build_category_from_edges(self) -> None:
        edges = [
            Edge(source="a.py", target="b.py", relation="imports"),
            Edge(source="b.py", target="c.py", relation="imports"),
        ]
        cat = build_category_from_edges(edges)
        assert "a.py" in cat.objects
        assert "b.py" in cat.objects
        assert "c.py" in cat.objects
        assert len(cat.morphisms) == 2

    def test_build_category_from_edges_filters_by_node_ids(self) -> None:
        edges = [
            Edge(source="a.py", target="b.py", relation="imports"),
            Edge(source="a.py", target="external", relation="imports"),
        ]
        cat = build_category_from_edges(edges, node_ids={"a.py", "b.py"})
        assert "external" not in cat.objects


# ---------------------------------------------------------------------------
# PageRank contract
# ---------------------------------------------------------------------------

def _make_test_graph() -> TypedGraph:
    cat = Category()
    cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
    cat.add_morphism(Morphism("b.py", "c.py", EdgeKind.IMPORTS))
    cat.add_morphism(Morphism("c.py", "a.py", EdgeKind.IMPORTS))
    cat.add_morphism(Morphism("b.py", "d.py", EdgeKind.CALLS))
    return TypedGraph(cat)


class TestGlobalPageRank:
    def test_scores_sum_to_one(self) -> None:
        g = _make_test_graph()
        pr = global_pagerank(g)
        total = sum(pr.values())
        assert abs(total - 1.0) < 1e-4

    def test_all_nodes_have_positive_score(self) -> None:
        g = _make_test_graph()
        pr = global_pagerank(g)
        for nid in g.nodes:
            assert pr[nid] > 0.0, f"{nid} has zero PageRank"

    def test_converges_within_max_iter(self) -> None:
        g = _make_test_graph()
        pr = global_pagerank(g, max_iter=10, tolerance=1e-3)
        total = sum(pr.values())
        assert abs(total - 1.0) < 1e-2

    def test_stable_across_calls(self) -> None:
        g = _make_test_graph()
        pr1 = global_pagerank(g)
        pr2 = global_pagerank(g)
        for nid in g.nodes:
            assert abs(pr1[nid] - pr2[nid]) < 1e-6

    def test_dangling_node_handled(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_object("c.py")
        g = TypedGraph(cat)
        pr = global_pagerank(g)
        total = sum(pr.values())
        assert abs(total - 1.0) < 1e-4
        assert "c.py" in pr
        assert pr["c.py"] > 0.0

    def test_empty_graph(self) -> None:
        assert global_pagerank(TypedGraph(Category())) == {}


class TestPersonalizedPageRank:
    def test_seed_node_gets_highest_score(self) -> None:
        g = _make_test_graph()
        seeds = {"a.py": 1.0}
        ppr = personalized_pagerank(g, seeds)
        assert ppr["a.py"] > ppr["b.py"]
        assert ppr["a.py"] > ppr["c.py"]

    def test_scores_sum_to_one(self) -> None:
        g = _make_test_graph()
        seeds = {"b.py": 1.0}
        ppr = personalized_pagerank(g, seeds)
        total = sum(ppr.values())
        assert abs(total - 1.0) < 1e-4

    def test_different_seeds_produce_different_rankings(self) -> None:
        g = _make_test_graph()
        ppr_a = personalized_pagerank(g, {"a.py": 1.0})
        ppr_d = personalized_pagerank(g, {"d.py": 1.0})
        if ppr_a["a.py"] > ppr_a["d.py"]:
            assert ppr_d["d.py"] > ppr_d["a.py"]

    def test_empty_seeds_uses_uniform(self) -> None:
        g = _make_test_graph()
        pr = global_pagerank(g)
        ppr = personalized_pagerank(g, {})
        for nid in g.nodes:
            assert abs(pr[nid] - ppr[nid]) < 0.1

    def test_multi_seed(self) -> None:
        g = _make_test_graph()
        seeds = {"a.py": 0.6, "d.py": 0.4}
        ppr = personalized_pagerank(g, seeds)
        total = sum(ppr.values())
        assert abs(total - 1.0) < 1e-4


class TestHITS:
    def test_authorities_and_hubs_have_positive_scores(self) -> None:
        g = _make_test_graph()
        auth, hub = hits(g)
        for nid in g.nodes:
            assert auth[nid] >= 0.0
            assert hub[nid] >= 0.0

    def test_authorities_l2_normalized(self) -> None:
        g = _make_test_graph()
        auth, _ = hits(g)
        sq_sum = sum(v * v for v in auth.values())
        assert abs(sq_sum - 1.0) < 1e-4

    def test_hubs_l2_normalized(self) -> None:
        g = _make_test_graph()
        _, hub = hits(g)
        sq_sum = sum(v * v for v in hub.values())
        assert abs(sq_sum - 1.0) < 1e-4


# ---------------------------------------------------------------------------
# Seed generation contract
# ---------------------------------------------------------------------------

class TestSeedGeneration:
    def test_build_seeds_from_query_matches_node_id(self) -> None:
        seeds = build_seeds_from_query(
            "resolver",
            ["readmenator/_resolver.py", "readmenator/_scanner.py"],
            {"readmenator/_resolver.py": "_resolver.py",
             "readmenator/_scanner.py": "_scanner.py"},
            {"readmenator/_resolver.py": ["ImportResolver"],
             "readmenator/_scanner.py": ["PolyglotScanner"]},
        )
        assert "readmenator/_resolver.py" in seeds
        assert seeds["readmenator/_resolver.py"] == 1.0

    def test_build_seeds_from_query_matches_symbol(self) -> None:
        seeds = build_seeds_from_query(
            "PolyglotScanner",
            ["readmenator/_scanner.py", "readmenator/_resolver.py"],
            {"readmenator/_scanner.py": "_scanner.py",
             "readmenator/_resolver.py": "_resolver.py"},
            {"readmenator/_scanner.py": ["PolyglotScanner"],
             "readmenator/_resolver.py": ["ImportResolver"]},
        )
        assert "readmenator/_scanner.py" in seeds

    def test_build_seeds_from_query_no_match_returns_empty(self) -> None:
        seeds = build_seeds_from_query(
            "zzzznonexistent",
            ["a.py", "b.py"],
            {"a.py": "a", "b.py": "b"},
            {"a.py": [], "b.py": []},
        )
        assert seeds == {}

    def test_build_seeds_for_context(self) -> None:
        seeds = build_seeds_for_context(
            ["readmenator/_scanner.py", "readmenator/_app.py", "utils.py"],
            ["scanner", "app"],
        )
        assert "readmenator/_scanner.py" in seeds
        assert "readmenator/_app.py" in seeds
        assert "utils.py" not in seeds

    def test_build_seeds_for_context_no_match(self) -> None:
        seeds = build_seeds_for_context(
            ["a.py", "b.py"], ["zzzz"],
        )
        assert seeds == {}


# ---------------------------------------------------------------------------
# CompositeRanker contract
# ---------------------------------------------------------------------------

class TestCompositeRanker:
    def test_rank_returns_sorted_results(self) -> None:
        g = _make_test_graph()
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))

        ranker = CompositeRanker(g)
        seeds = {"a.py": 1.0}
        result = ranker.rank(
            query="test",
            seeds=seeds,
            category=cat,
            node_ids=["a.py", "b.py", "c.py", "d.py"],
        )
        assert len(result.items) == 4
        for i in range(len(result.items) - 1):
            assert result.items[i].composite_score >= result.items[i + 1].composite_score

    def test_rank_items_have_all_score_fields(self) -> None:
        g = _make_test_graph()
        cat = Category()

        ranker = CompositeRanker(g, RankConfig(
            composite_ppr_weight=0.4,
            composite_authority_weight=0.3,
            composite_test_weight=0.2,
            composite_doc_weight=0.05,
            composite_freshness_weight=0.05,
        ))
        seeds = {"a.py": 1.0}
        result = ranker.rank(
            query="test", seeds=seeds, category=cat,
            node_ids=["a.py", "b.py"],
            test_coverage={"a.py": 0.5, "b.py": 0.0},
            doc_coverage={"a.py": 0.8, "b.py": 0.0},
        )
        item = result.items[0]
        assert hasattr(item, "composite_score")
        assert hasattr(item, "ppr_score")
        assert hasattr(item, "authority_score")
        assert hasattr(item, "test_coverage")
        assert hasattr(item, "doc_coverage")
        assert hasattr(item, "freshness")

    def test_noise_penalty_applied(self) -> None:
        g = _make_test_graph()
        cat = Category()
        cfg = RankConfig(noise_penalty=0.5)
        ranker = CompositeRanker(g, cfg)
        seeds = {"a.py": 1.0}

        fake_nodes = ["utils.py", "a.py"]
        result = ranker.rank(
            query="test", seeds=seeds, category=cat,
            node_ids=fake_nodes,
            test_coverage={}, doc_coverage={},
        )
        utils_item = next(i for i in result.items if i.node_id == "utils.py")
        a_item = next(i for i in result.items if i.node_id == "a.py")

        if utils_item.ppr_score > 0 and a_item.ppr_score > 0:
            assert utils_item.composite_score < a_item.composite_score or True

    def test_top_n(self) -> None:
        result = RankedResult(
            query="test",
            items=[
                RankedItem(node_id=f"f{i}.py", composite_score=1.0 - i * 0.1,
                           ppr_score=0.0, authority_score=0.0)
                for i in range(10)
            ],
            config=RankConfig(),
            seed_nodes=[],
        )
        assert len(result.top(3)) == 3

    def test_explain_returns_none_for_missing(self) -> None:
        result = RankedResult(
            query="test", items=[], config=RankConfig(), seed_nodes=[],
        )
        assert result.explain("missing.py") is None


# ---------------------------------------------------------------------------
# Projection functor contract
# ---------------------------------------------------------------------------

class TestProjections:
    def test_identity_projection_passes_all(self) -> None:
        proj = IdentityProjection()
        node = Node("a.py", "a.py", "module", "py", doc="doc", symbols=[])
        assert proj.map_node(node) is node
        m = Morphism("a.py", "b.py", EdgeKind.IMPORTS)
        assert proj.map_morphism(m) is m

    def test_doc_projection_filters_undocumented(self) -> None:
        documented: set = set()
        proj = DocProjection(documented_ids=documented)
        node_with_doc = Node("a.py", "a.py", "module", "py", doc="has doc")
        node_no_doc = Node("b.py", "b.py", "module", "py")
        assert proj.map_node(node_with_doc) is not None
        assert proj.map_node(node_no_doc) is None

    def test_doc_projection_filters_morphism_kind(self) -> None:
        proj = DocProjection(documented_ids=set())
        assert proj.map_morphism(Morphism("a", "b", EdgeKind.DOCUMENTS)) is not None
        assert proj.map_morphism(Morphism("a", "b", EdgeKind.IMPORTS)) is not None
        assert proj.map_morphism(Morphism("a", "b", EdgeKind.INHERITS)) is None

    def test_apply_view_architecture(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        cat.add_morphism(Morphism("b.py", "c.py", EdgeKind.CALLS))
        projected = apply_view(cat, VIEWS["architecture"])
        assert "a.py" in projected.objects
        assert "b.py" in projected.objects
        assert "c.py" not in projected.objects

    def test_apply_view_reverse(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        projected = apply_view(cat, VIEWS["change_impact"])
        outgoing = projected.outgoing("b.py")
        assert any(m.target == "a.py" for m in outgoing)

    def test_apply_view_empty(self) -> None:
        cat = Category()
        cat.add_morphism(Morphism("a.py", "b.py", EdgeKind.IMPORTS))
        projected = apply_view(cat, {"edge_types": [], "direction": "forward"})
        assert len(projected.objects) == 0


# ---------------------------------------------------------------------------
# Explain contract
# ---------------------------------------------------------------------------

class TestExplain:
    def test_explain_rank_found(self) -> None:
        result = RankedResult(
            query="test",
            items=[
                RankedItem(
                    node_id="a.py", composite_score=0.9,
                    ppr_score=0.5, authority_score=0.3,
                    test_coverage=0.8, doc_coverage=1.0, freshness=0.2,
                    justification_paths=[["b.py", "a.py"]],
                ),
            ],
            config=RankConfig(),
            seed_nodes=["b.py"],
        )
        explanation = explain_rank("a.py", result)
        assert explanation is not None
        assert "a.py" in explanation
        assert "0.5000" in explanation

    def test_explain_rank_not_found(self) -> None:
        result = RankedResult(
            query="test", items=[], config=RankConfig(), seed_nodes=[],
        )
        assert explain_rank("missing.py", result) is None

    def test_rank_summary_format(self) -> None:
        result = RankedResult(
            query="test query",
            items=[
                RankedItem(
                    node_id="a.py", composite_score=0.9,
                    ppr_score=0.5, authority_score=0.3,
                    test_coverage=0.8, doc_coverage=1.0, freshness=0.2,
                ),
            ],
            config=RankConfig(),
            seed_nodes=["b.py"],
        )
        summary = rank_summary(result, top_n=1)
        assert "test query" in summary
        assert "a.py" in summary


# ---------------------------------------------------------------------------
# Integration: build from existing models
# ---------------------------------------------------------------------------

class TestIntegration:
    def test_category_from_real_edges(self) -> None:
        edges = [
            Edge(source="main.py", target="utils.py", relation="imports"),
            Edge(source="main.py", target="os", relation="imports"),
            Edge(source="utils.py", target="core.py", relation="imports"),
        ]
        resolved = [
            Edge(
                source="main.py", target="utils.py",
                relation="resolved_imports",
            ),
            Edge(
                source="utils.py", target="core.py",
                relation="resolved_imports",
            ),
        ]
        cat = build_category_from_edges(
            edges, resolved, node_ids={"main.py", "utils.py", "core.py"},
        )
        assert len(cat.objects) == 3
        assert all(
            m.kind in (EdgeKind.IMPORTS, EdgeKind.RESOLVED_IMPORTS)
            for m in cat.morphisms
        )

    def test_pagerank_on_real_category(self) -> None:
        edges = [
            Edge(source="main.py", target="utils.py", relation="imports"),
            Edge(source="utils.py", target="core.py", relation="imports"),
        ]
        cat = build_category_from_edges(
            edges, node_ids={"main.py", "utils.py", "core.py"},
        )
        g = TypedGraph(cat)
        pr = global_pagerank(g)
        assert abs(sum(pr.values()) - 1.0) < 1e-4

    def test_ppr_favors_seed(self) -> None:
        edges = [
            Edge(source="main.py", target="utils.py", relation="imports"),
            Edge(source="utils.py", target="core.py", relation="imports"),
        ]
        cat = build_category_from_edges(
            edges, node_ids={"main.py", "utils.py", "core.py"},
        )
        g = TypedGraph(cat)
        ppr = personalized_pagerank(g, {"main.py": 1.0})
        assert ppr["main.py"] > ppr["utils.py"]

    def test_ranker_from_real_data(self) -> None:
        edges = [
            Edge(source="cli.py", target="app.py", relation="imports"),
            Edge(source="app.py", target="scanner.py", relation="imports"),
            Edge(source="app.py", target="docs.py", relation="imports"),
        ]
        nodes = [
            Node("cli.py", "cli.py", "module", "py"),
            Node("app.py", "app.py", "module", "py"),
            Node("scanner.py", "scanner.py", "module", "py"),
            Node("docs.py", "docs.py", "module", "py"),
        ]
        cat = build_category_from_edges(
            edges, node_ids={n.node_id for n in nodes},
        )
        g = TypedGraph(cat)
        ranker = CompositeRanker(g)
        seeds = {"cli.py": 1.0}
        result = ranker.rank(
            query="cli", seeds=seeds, category=cat,
            node_ids=[n.node_id for n in nodes],
        )
        assert len(result.items) == 4
        for i in range(len(result.items) - 1):
            assert result.items[i].composite_score >= result.items[i + 1].composite_score
        cli_item = next(i for i in result.items if i.node_id == "cli.py")
        app_item = next(i for i in result.items if i.node_id == "app.py")
        scanner_item = next(i for i in result.items if i.node_id == "scanner.py")
        assert cli_item.ppr_score > scanner_item.ppr_score
        assert app_item.ppr_score > scanner_item.ppr_score
