import unittest

from readmenator._config import Config
from readmenator._concepts import ConceptExtractor, verb_for_relation
from readmenator._models import Edge, Node, Symbol


def _node(fid: str, symbols: list, doc: str = "") -> Node:
    """Build a file node with the given symbols and doc."""
    return Node(
        node_id=fid,
        label=fid.split("/")[-1],
        kind="module",
        language="python",
        doc=doc,
        symbols=symbols,
    )


class TestConceptGraphContract(unittest.TestCase):
    def test_concept_nouns_map_to_file_sets(self) -> None:
        """Noun tokens become concepts mapping to file sets."""
        config = Config(CONCEPT_MIN_FILES=2, CONCEPT_MAX_CONCEPTS=50)
        nodes = [
            _node("pkg/wiki.py", [Symbol("WikiGenerator", "class", 1)]),
            _node("pkg/wiki_index.py", [Symbol("WikiIndexer", "class", 2)]),
            _node("pkg/video.py", [Symbol("VideoRenderer", "class", 3)]),
        ]
        graph = ConceptExtractor(config).extract(nodes, [])
        names = {c.name for c in graph.concepts}
        self.assertIn("wiki", names)
        wiki = next(c for c in graph.concepts if c.name == "wiki")
        self.assertEqual(len(wiki.file_ids), 2)
        self.assertEqual(wiki.confidence, "EXTRACTED")

    def test_concept_verbs_come_from_structural_edges(self) -> None:
        """Structural imports aggregate into verb relations."""
        config = Config(CONCEPT_MIN_FILES=1, CONCEPT_MAX_CONCEPTS=50)
        nodes = [
            _node("pkg/wiki.py", [Symbol("WikiGenerator", "class", 1)]),
            _node("pkg/video.py", [Symbol("VideoRenderer", "class", 1)]),
        ]
        edges = [Edge("pkg/wiki.py", "pkg/video.py", "imports", "EXTRACTED")]
        graph = ConceptExtractor(config).extract(nodes, edges)
        verbs = {(r.source, r.target, r.verb) for r in graph.relations}
        self.assertTrue(any(v[2] == "consumes" for v in verbs))
        self.assertEqual(verb_for_relation("calls"), "invokes")
        self.assertEqual(verb_for_relation("inherits"), "extends")
        self.assertEqual(
            verb_for_relation("resolved_imports"), "depends_on"
        )

    def test_concept_atomic_breakdown_splits_camelcase(self) -> None:
        """CamelCase symbols decompose into atomic noun tokens."""
        config = Config(CONCEPT_MIN_FILES=1, CONCEPT_MAX_CONCEPTS=50)
        nodes = [_node("pkg/a.py", [Symbol("WikiGenerator", "class", 1)])]
        graph = ConceptExtractor(config).extract(nodes, [])
        names = {c.name for c in graph.concepts}
        self.assertIn("wiki", names)
        self.assertIn("generator", names)

    def test_concept_deterministic_ordering(self) -> None:
        """Identical input yields identical concept order."""
        config = Config()
        nodes = [
            _node("b.py", [Symbol("AlphaBeta", "class", 1)]),
            _node("a.py", [Symbol("AlphaGamma", "class", 1)]),
        ]
        first = ConceptExtractor(config).extract(nodes, [])
        second = ConceptExtractor(config).extract(list(reversed(nodes)), [])
        self.assertEqual(
            [c.name for c in first.concepts],
            [c.name for c in second.concepts],
        )

    def test_concept_disabled_returns_empty_graph(self) -> None:
        """Disabled flag bypasses extraction without errors."""
        config = Config(CONCEPT_ENABLED=False)
        nodes = [_node("a.py", [Symbol("WikiGenerator", "class", 1)])]
        graph = ConceptExtractor(config).extract(nodes, [])
        self.assertEqual(graph.concepts, [])
        self.assertEqual(graph.relations, [])
        self.assertEqual(graph.dialectic_questions, [])

    def test_concept_dialectic_questions_for_overlap(self) -> None:
        """Overlapping concepts emit thesis/antithesis prompts."""
        config = Config(
            CONCEPT_MIN_FILES=1,
            CONCEPT_MAX_CONCEPTS=50,
            CONCEPT_DIALECTIC_MAX=10,
        )
        nodes = [
            _node("a.py", [Symbol("AlphaShared", "class", 1)]),
            _node("b.py", [Symbol("AlphaShared", "class", 1)]),
            _node("c.py", [Symbol("BetaShared", "class", 1)]),
        ]
        nodes[0].symbols.append(Symbol("BetaShared", "class", 5))
        nodes[1].symbols.append(Symbol("BetaShared", "class", 6))
        graph = ConceptExtractor(config).extract(nodes, [])
        self.assertTrue(graph.dialectic_questions)
        self.assertIn("Thesis", graph.dialectic_questions[0])


if __name__ == "__main__":
    unittest.main()
