import unittest

from readmenator._config import Config
from readmenator._dataflow import DataflowAnalyzer
from readmenator._models import Node, Symbol


def _node(node_id: str, funcs: list) -> Node:
    return Node(
        node_id=node_id, label=node_id.split("/")[-1], kind="module",
        language="c", symbols=[
            Symbol(name=name, kind="function", line=line) for name, line in funcs
        ],
    )


def _analyze(body: str) -> list:
    config = Config()
    analyzer = DataflowAnalyzer(config)
    content = "int f(void)\n{\n" + body + "\n}\n"
    node = _node("a.c", [("f", 1)])
    return analyzer.analyze([node], {"a.c": content})


class TestDataflowContract(unittest.TestCase):
    def test_config_defaults(self) -> None:
        config = Config()
        self.assertTrue(config.DATAFLOW_ENABLED)
        self.assertEqual(config.DATAFLOW_MAX_ISSUES, 50)

    def test_config_immutable(self) -> None:
        from dataclasses import FrozenInstanceError
        config = Config()
        with self.assertRaises(FrozenInstanceError):
            config.DATAFLOW_ENABLED = False  # type: ignore[misc]

    def test_uninit_use_detected(self) -> None:
        issues = _analyze("    int x;\n    return x;\n")
        kinds = [i.kind for i in issues]
        self.assertIn("UNINIT_USE", kinds)
        hit = [i for i in issues if i.kind == "UNINIT_USE"][0]
        self.assertEqual(hit.variable, "x")
        self.assertEqual(hit.function, "f")
        self.assertEqual(hit.confidence, "INFERRED")

    def test_initialized_use_clean(self) -> None:
        issues = _analyze("    int x = 5;\n    return x;\n")
        self.assertEqual([i for i in issues if i.variable == "x"], [])

    def test_params_count_as_initialized(self) -> None:
        config = Config()
        analyzer = DataflowAnalyzer(config)
        content = "int add(int a, int b)\n{\n    return a + b;\n}\n"
        node = _node("a.c", [("add", 1)])
        issues = analyzer.analyze([node], {"a.c": content})
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_scanf_addr_counts_as_init(self) -> None:
        issues = _analyze("    int x;\n    scanf(\"%d\", &x);\n    return x;\n")
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_dead_store_detected(self) -> None:
        issues = _analyze("    int x = 5;\n    x = 6;\n    return 0;\n")
        kinds = [(i.kind, i.line) for i in issues if i.variable == "x"]
        self.assertIn(("DEAD_STORE", 4), kinds)

    def test_read_store_clean(self) -> None:
        issues = _analyze("    int x = 5;\n    x = 6;\n    return x;\n")
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_unchecked_alloc_detected(self) -> None:
        issues = _analyze(
            "    char *p;\n    p = malloc(64);\n    p[0] = 0;\n    return p;\n"
        )
        kinds = [i.kind for i in issues if i.variable == "p"]
        self.assertIn("UNCHECKED_ALLOC", kinds)

    def test_checked_alloc_clean(self) -> None:
        issues = _analyze(
            "    char *p;\n    p = malloc(64);\n    if (!p) return 0;\n    return 1;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNCHECKED_ALLOC"])

    def test_disabled_returns_empty(self) -> None:
        config = Config(DATAFLOW_ENABLED=False)
        analyzer = DataflowAnalyzer(config)
        node = _node("a.c", [("f", 1)])
        content = "int f(void)\n{\n    int x;\n    return x;\n}\n"
        self.assertEqual(analyzer.analyze([node], {"a.c": content}), [])

    def test_missing_content_skipped(self) -> None:
        config = Config()
        analyzer = DataflowAnalyzer(config)
        self.assertEqual(analyzer.analyze([_node("a.c", [("f", 1)])], {}), [])

    def test_issue_cap_respected(self) -> None:
        config = Config(DATAFLOW_MAX_ISSUES=3)
        analyzer = DataflowAnalyzer(config)
        body = "".join(f"    int v{i};\n    return v{i};\n" for i in range(10))
        content = "int f(void)\n{\n" + body + "}\n"
        node = _node("a.c", [("f", 1)])
        issues = analyzer.analyze([node], {"a.c": content})
        self.assertLessEqual(len(issues), 3)

    def test_plain_assignment_is_not_a_declaration(self) -> None:
        issues = _analyze("    g_true = make_sym(1);\n    return g_true;\n")
        self.assertFalse([i for i in issues if i.variable == "rue"])
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_subscript_store_counts_as_init(self) -> None:
        issues = _analyze(
            "    char buf[16];\n    buf[0] = 65;\n    return buf[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_asm_output_counts_as_init(self) -> None:
        issues = _analyze(
            '    long ret;\n    __asm__ volatile("syscall" : "=a"(ret) : "a"(1) : "rcx");\n'
            "    return ret;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_fd_lt_zero_counts_as_checked(self) -> None:
        issues = _analyze(
            "    int fd;\n    fd = socket(1, 2, 3);\n    if (fd < 0) return -1;\n    return fd;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNCHECKED_ALLOC"])

    def test_map_failed_counts_as_checked(self) -> None:
        issues = _analyze(
            "    void *m;\n    m = mmap(0, 8, 1, 2, -1, 0);\n"
            "    if (m == MAP_FAILED) return 0;\n    return 1;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNCHECKED_ALLOC"])

    def test_member_null_check_counts(self) -> None:
        issues = _analyze(
            "    b->data = calloc(4, 1);\n"
            "    if (!b->data) return;\n"
            "    b->len = 4;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNCHECKED_ALLOC"])

    def test_loop_carried_var_not_dead(self) -> None:
        issues = _analyze(
            "    int first = 1;\n"
            "    while (n) {\n"
            "        if (!first) put();\n"
            "        first = 0;\n"
            "        n--;\n"
            "    }\n"
            "    return;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_line_numbers_survive_subscript_stores(self) -> None:
        issues = _analyze(
            "    char b[8];\n"
            "    b[0] = 65;\n"
            "    int u;\n"
            "    return u;\n"
        )
        hits = [i for i in issues if i.kind == "UNINIT_USE" and i.variable == "u"]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].line, 6)

    def test_member_store_not_local_assign(self) -> None:
        issues = _analyze(
            "    obj.count = 0;\n    return obj.count;\n"
        )
        self.assertFalse([i for i in issues if i.variable == "count"])

    def test_array_arg_to_filler_counts_as_init(self) -> None:
        issues = _analyze(
            "    unsigned char b[32];\n"
            "    fill(b, 32);\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_array_arg_to_readonly_still_uninit(self) -> None:
        issues = _analyze(
            "    unsigned char b[32];\n"
            "    return strlen(b);\n"
        )
        self.assertTrue([i for i in issues if i.kind == "UNINIT_USE"])

    def test_array_filled_in_decl_init_call(self) -> None:
        issues = _analyze(
            "    unsigned char b[16];\n"
            "    int n = fill(b, 16);\n"
            "    return b[0] + n;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_static_never_uninit(self) -> None:
        issues = _analyze(
            "    static int total;\n"
            "    return total;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_derived_pointer_not_dead(self) -> None:
        config = Config()
        analyzer = DataflowAnalyzer(config)
        content = (
            "void f(int *set)\n{\n"
            "    unsigned long *bits = (unsigned long *)set;\n"
            "    bits[0] = 1;\n"
            "    return;\n}\n"
        )
        node = _node("a.c", [("f", 1)])
        issues = analyzer.analyze([node], {"a.c": content})
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_sizeof_is_not_a_read(self) -> None:
        issues = _analyze(
            "    char b[64];\n"
            "    size_t m = sizeof b - 1;\n"
            "    fill(b, m);\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_block_comment_malloc_ignored(self) -> None:
        issues = _analyze(
            "    size_t n = x ? x : 1; /* avoid malloc(0) */\n"
            "    int *p = malloc(n);\n"
            "    if (!p) return 0;\n"
            "    return 1;\n"
        )
        self.assertFalse([i for i in issues if i.variable == "n"])

    def test_address_alias_pointer_not_dead(self) -> None:
        config = Config()
        analyzer = DataflowAnalyzer(config)
        content = (
            "int f(void)\n{\n"
            "    int a = 0;\n"
            "    int *p = &a;\n"
            "    *p = 1;\n"
            "    return a;\n}\n"
        )
        node = _node("a.c", [("f", 1)])
        issues = analyzer.analyze([node], {"a.c": content})
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_array_store_before_read_suppresses_uninit(self) -> None:
        issues = _analyze(
            "    char b[8];\n"
            "    b[0] = 65;\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_same_line_use_not_dead(self) -> None:
        issues = _analyze(
            "    int t;\n"
            "    t = f(); g(t);\n"
            "    return;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_same_line_only_assign_is_dead(self) -> None:
        issues = _analyze(
            "    int t;\n"
            "    t = 1;\n"
            "    return;\n"
        )
        self.assertTrue([i for i in issues if i.kind == "DEAD_STORE"])

    def test_alias_pointer_store_initializes_array(self) -> None:
        issues = _analyze(
            "    char b[16];\n"
            "    char *d = b;\n"
            "    *d = 65;\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_inline_alias_fill_suppresses_uninit(self) -> None:
        issues = _analyze(
            "    char b[16];\n"
            "    { char *d = b; *d = 65; }\n"
            "    b[0] = 0;\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_function_pointer_call_counts_as_use(self) -> None:
        issues = _analyze(
            "    void (*cb)(void) = setup();\n"
            "    if (cb) cb();\n"
            "    return;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_plain_call_is_not_a_local_use(self) -> None:
        issues = _analyze(
            "    setup();\n"
            "    return;\n"
        )
        self.assertEqual(issues, [])

    def test_local_struct_does_not_truncate_span(self) -> None:
        from readmenator._models import Node, Symbol
        config = Config()
        analyzer = DataflowAnalyzer(config)
        content = (
            "void f(void)\n"
            "{\n"
            "    int x = 1;\n"
            "    struct S { int a; };\n"
            "    use(x);\n"
            "    return;\n"
            "}\n"
        )
        node = Node("a.c", "a.c", "module", "c", symbols=[
            Symbol("f", "function", 1),
            Symbol("S", "struct", 4),
        ])
        lines = content.split("\n")
        depths = analyzer._brace_depths(lines)
        spans = analyzer._function_spans(node, len(lines), depths)
        self.assertEqual(spans, [("f", 0, 8)])
        issues = analyzer.analyze([node], {"a.c": content})
        self.assertFalse([i for i in issues if i.variable == "x"])

    def test_file_scope_symbol_still_bounds_span(self) -> None:
        from readmenator._models import Node, Symbol
        config = Config()
        analyzer = DataflowAnalyzer(config)
        content = "int f(void)\n{\n    return 1;\n}\nint g = 2;\nint h(void)\n{\n    return g;\n}\n"
        node = Node("a.c", "a.c", "module", "c", symbols=[
            Symbol("f", "function", 1),
            Symbol("g", "variable", 5),
            Symbol("h", "function", 6),
        ])
        lines = content.split("\n")
        depths = analyzer._brace_depths(lines)
        spans = analyzer._function_spans(node, len(lines), depths)
        self.assertEqual(spans, [("f", 0, 4), ("h", 5, 10)])

    def test_url_string_does_not_truncate_line(self) -> None:
        issues = _analyze(
            "    int rc;\n"
            "    run(\"http://x\", &rc);\n"
            "    return rc;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_assert_macro_counts_as_null_check(self) -> None:
        issues = _analyze(
            "    FILE *f = fopen(p, \"w\");\n"
            "    assert_non_null(f);\n"
            "    return;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNCHECKED_ALLOC"])

    def test_multiline_call_assigns_array_arg(self) -> None:
        issues = _analyze(
            "    unsigned char b[32];\n"
            "    fill(b,\n"
            "         32);\n"
            "    return b[0];\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])

    def test_address_taken_suppresses_dead_store(self) -> None:
        issues = _analyze(
            "    struct L l;\n"
            "    reg(&l);\n"
            "    return;\n"
        )
        self.assertFalse([i for i in issues if i.kind == "DEAD_STORE"])

    def test_member_store_initializes_base(self) -> None:
        issues = _analyze(
            "    struct K k;\n"
            "    k.field = 1;\n"
            "    use(k.field);\n"
        )
        self.assertFalse([i for i in issues if i.kind == "UNINIT_USE"])


if __name__ == "__main__":
    unittest.main()
