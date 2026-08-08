from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Optional, Set

from readmenator._config import Config
from readmenator._models import Edge, Node, Symbol


_CLASS_LIKE_KINDS = frozenset({
    "class", "struct", "interface", "trait", "enum", "record",
    "protocol", "extension",
})


_LANGUAGE_CODE_GENERATORS: Dict[str, str] = {
    "cpp": "cpp",
    "java": "java",
    "csharp": "csharp",
    "python": "python",
    "go": "go",
    "rust": "rust",
    "php": "php",
    "kotlin": "kotlin",
    "scala": "scala",
    "swift": "swift",
    "dart": "dart",
    "ruby": "ruby",
}


class UmlGenerator:

    def __init__(self, config: Config) -> None:
        self._config = config

    def render_mermaid_class_diagram(
        self,
        nodes: List[Node],
        edges: List[Edge],
    ) -> str:
        class_nodes: List[tuple] = []
        for node in nodes:
            for sym in node.symbols:
                if sym.kind in _CLASS_LIKE_KINDS:
                    class_nodes.append((node, sym))
        if not class_nodes:
            return ""

        max_classes = self._config.UML_MAX_CLASSES
        if len(class_nodes) > max_classes:
            class_nodes = class_nodes[:max_classes]

        lines: List[str] = ["classDiagram"]
        class_ids: Set[str] = set()

        for node, sym in class_nodes:
            class_id = self._sanitize_id(f"{node.label}_{sym.name}")
            class_ids.add(class_id)

            lines.append(f"  class {class_id} {{")
            lines.append(f"    <<{sym.kind}>>")

            methods = [
                s for s in node.symbols
                if s.kind in ("function", "method")
            ]
            for method in methods[:10]:
                params = ""
                if method.signature:
                    sig = method.signature
                    paren = sig.find("(")
                    if paren >= 0:
                        params = sig[paren:].rstrip("{: ")
                lines.append(f"    +{method.name}{params}")

            lines.append("  }")

        inherit_edges: Dict[str, Set[str]] = defaultdict(set)
        for edge in edges:
            if edge.relation == "inherits":
                for node in nodes:
                    if node.label == edge.source.split("/")[-1]:
                        for sym in node.symbols:
                            if sym.name == edge.source.split(".")[-1]:
                                src_id = self._sanitize_id(
                                    f"{node.label}_{sym.name}"
                                )
                                tgt_id = self._sanitize_id(
                                    f"{edge.target}_{sym.name}"
                                )
                                if src_id not in class_ids:
                                    class_ids.add(src_id)
                                if tgt_id not in class_ids:
                                    class_ids.add(tgt_id)
                                inherit_edges[src_id].add(tgt_id)

        for src_id, tgt_ids in inherit_edges.items():
            for tgt_id in tgt_ids:
                if src_id in class_ids and tgt_id in class_ids:
                    lines.append(f"  {src_id} --|> {tgt_id}")

        import_rel: Set[tuple] = set()
        for edge in edges:
            if edge.relation in ("imports", "resolved_imports"):
                src_node = self._find_node(nodes, edge.source)
                tgt_node = self._find_node(nodes, edge.target)
                if src_node and tgt_node:
                    for s_sym in src_node.symbols:
                        if s_sym.kind in _CLASS_LIKE_KINDS:
                            for t_sym in tgt_node.symbols:
                                if t_sym.kind in _CLASS_LIKE_KINDS:
                                    sid = self._sanitize_id(
                                        f"{src_node.label}_{s_sym.name}"
                                    )
                                    tid = self._sanitize_id(
                                        f"{tgt_node.label}_{t_sym.name}"
                                    )
                                    if sid != tid and sid in class_ids and tid in class_ids:
                                        import_rel.add((sid, tid))

        for sid, tid in sorted(import_rel):
            lines.append(f"  {sid} --> {tid} : uses")

        return "\n".join(lines)

    def generate_code(
        self,
        nodes: List[Node],
        edges: List[Edge],
        target_language: str,
    ) -> str:
        target = target_language.lower().lstrip("-")
        if target not in _LANGUAGE_CODE_GENERATORS:
            return f"// Unknown target language: {target_language}"

        generator = _get_code_generator(target)
        class_symbols: List[tuple] = []
        for node in nodes:
            for sym in node.symbols:
                if sym.kind in _CLASS_LIKE_KINDS:
                    methods = [
                        s for s in node.symbols
                        if s.kind in ("function", "method")
                    ]
                    class_symbols.append((node, sym, methods))

        return generator(class_symbols, nodes, edges)

    @staticmethod
    def _sanitize_id(raw: str) -> str:
        sanitized = ""
        for ch in raw:
            if ch.isalnum() or ch == "_":
                sanitized += ch
            else:
                sanitized += "_"
        if sanitized and sanitized[0].isdigit():
            sanitized = "n_" + sanitized
        return sanitized

    @staticmethod
    def _find_node(nodes: List[Node], node_id: str) -> Optional[Node]:
        for n in nodes:
            if n.node_id == node_id:
                return n
        return None


def _get_code_generator(language: str):
    generators = {
        "cpp": _generate_cpp,
        "java": _generate_java,
        "csharp": _generate_csharp,
        "python": _generate_python,
        "go": _generate_go,
        "rust": _generate_rust,
        "php": _generate_php,
        "kotlin": _generate_kotlin,
        "scala": _generate_scala,
        "swift": _generate_swift,
        "dart": _generate_dart,
        "ruby": _generate_ruby,
    }
    return generators.get(language, _generate_python)


def _type_map_py_to_target(target: str, py_type_hint: str) -> str:
    if not py_type_hint:
        return ""
    mapping: Dict[str, Dict[str, str]] = {
        "cpp": {"int": "int", "float": "double", "str": "std::string",
                "bool": "bool", "list": "std::vector", "dict": "std::map",
                "None": "void", "bytes": "std::vector<uint8_t>",
                "tuple": "std::tuple"},
        "java": {"int": "int", "float": "double", "str": "String",
                 "bool": "boolean", "list": "List", "dict": "Map",
                 "None": "void", "bytes": "byte[]", "tuple": "Object[]"},
        "csharp": {"int": "int", "float": "double", "str": "string",
                   "bool": "bool", "list": "List", "dict": "Dictionary",
                   "None": "void", "bytes": "byte[]", "tuple": "Tuple"},
        "go": {"int": "int", "float": "float64", "str": "string",
               "bool": "bool", "list": "[]interface{}", "dict": "map[string]interface{}",
               "None": "", "bytes": "[]byte", "tuple": "[]interface{}"},
        "rust": {"int": "i32", "float": "f64", "str": "String",
                 "bool": "bool", "list": "Vec", "dict": "HashMap",
                 "None": "()", "bytes": "Vec<u8>", "tuple": "(,)"},
        "php": {"int": "int", "float": "float", "str": "string",
                "bool": "bool", "list": "array", "dict": "array",
                "None": "void", "bytes": "string", "tuple": "array"},
        "kotlin": {"int": "Int", "float": "Double", "str": "String",
                   "bool": "Boolean", "list": "List", "dict": "Map",
                   "None": "Unit", "bytes": "ByteArray", "tuple": "Array<Any>"},
        "scala": {"int": "Int", "float": "Double", "str": "String",
                  "bool": "Boolean", "list": "List", "dict": "Map",
                  "None": "Unit", "bytes": "Array[Byte]", "tuple": "Tuple"},
        "swift": {"int": "Int", "float": "Double", "str": "String",
                  "bool": "Bool", "list": "Array", "dict": "Dictionary",
                  "None": "Void", "bytes": "Data", "tuple": "()"},
        "dart": {"int": "int", "float": "double", "str": "String",
                 "bool": "bool", "list": "List", "dict": "Map",
                 "None": "void", "bytes": "Uint8List", "tuple": "List"},
        "ruby": {"int": "Integer", "float": "Float", "str": "String",
                 "bool": "Boolean", "list": "Array", "dict": "Hash",
                 "None": "nil", "bytes": "String", "tuple": "Array"},
    }
    lang_map = mapping.get(target, {})
    return lang_map.get(py_type_hint, py_type_hint)


def _generate_cpp(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated C++ class declarations from ReadMenator UML analysis", ""]
    lines.append("#include <string>")
    lines.append("#include <vector>")
    lines.append("#include <map>")
    lines.append("#include <memory>")
    lines.append("")
    for node, sym, methods in class_symbols:
        kind = "class" if sym.kind in ("class", "struct", "record") else sym.kind
        lines.append(f"{kind} {_safe_name(sym.name)} {{")
        lines.append("public:")
        for method in methods[:10]:
            ret = "void"
            params = _extract_params(method.signature)
            lines.append(f"    {ret} {_safe_name(method.name)}({_cpp_params(params)});")
        if not methods:
            lines.append(f"    // No methods extracted from source file")
        lines.append("};")
        lines.append("")
    return "\n".join(lines)


def _cpp_params(params: str) -> str:
    if not params:
        return ""
    parts = params.replace("(", "").replace(")", "").split(",")
    result = []
    for p in parts:
        p = p.strip()
        if ":" in p:
            name, type_hint = p.split(":", 1)
            result.append(f"{_type_map_py_to_target('cpp', type_hint.strip())} {name.strip()}")
        elif p:
            result.append(f"auto {p}")
    return ", ".join(result)


def _generate_java(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Java class declarations from ReadMenator UML analysis", ""]
    lines.append("import java.util.List;")
    lines.append("import java.util.Map;")
    lines.append("")
    for node, sym, methods in class_symbols:
        kind = "class"
        if sym.kind == "interface":
            kind = "interface"
        elif sym.kind in ("enum",):
            kind = "enum"
        lines.append(f"public {kind} {_safe_name(sym.name)} {{")
        for method in methods[:10]:
            params = _extract_params(method.signature)
            java_params = _java_params(params)
            lines.append(f"    public void {_safe_name(method.name)}({java_params}) {{ }}")
        if not methods:
            lines.append(f"    // No methods extracted")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _java_params(params: str) -> str:
    if not params:
        return ""
    parts = params.replace("(", "").replace(")", "").split(",")
    result = []
    for p in parts:
        p = p.strip()
        if ":" in p:
            name, type_hint = p.split(":", 1)
            result.append(f"{_type_map_py_to_target('java', type_hint.strip())} {name.strip()}")
        elif p:
            result.append(f"Object {p}")
    return ", ".join(result)


def _generate_csharp(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated C# class declarations from ReadMenator UML analysis", ""]
    lines.append("using System;")
    lines.append("using System.Collections.Generic;")
    lines.append("")
    for node, sym, methods in class_symbols:
        kind = "class"
        if sym.kind == "interface":
            kind = "interface"
        elif sym.kind in ("struct", "record"):
            kind = sym.kind
        elif sym.kind == "enum":
            kind = "enum"
        lines.append(f"public {kind} {_safe_name(sym.name)} {{")
        for method in methods[:10]:
            params = _extract_params(method.signature)
            cs_params = _cs_params(params)
            lines.append(f"    public void {_safe_name(method.name)}({cs_params}) {{ }}")
        if not methods:
            lines.append(f"    // No methods extracted")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _cs_params(params: str) -> str:
    if not params:
        return ""
    parts = params.replace("(", "").replace(")", "").split(",")
    result = []
    for p in parts:
        p = p.strip()
        if ":" in p:
            name, type_hint = p.split(":", 1)
            result.append(f"{_type_map_py_to_target('csharp', type_hint.strip())} {name.strip()}")
        elif p:
            result.append(f"object {p}")
    return ", ".join(result)


def _generate_python(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["# Generated Python class declarations from ReadMenator UML analysis", ""]
    lines.append("from typing import List, Dict, Optional, Any")
    lines.append("")
    for node, sym, methods in class_symbols:
        kind = "class"
        if sym.kind == "enum":
            from enum import Enum  # noqa: just for reference
            lines.append(f"from enum import Enum")
            lines.append("")
        lines.append(f"{kind} {_safe_name(sym.name)}:")
        has_body = False
        for method in methods[:10]:
            if method.name == "__init__":
                params = _extract_params(method.signature).replace("self, ", "").replace("self", "")
                if params:
                    lines.append(f"    def __init__(self, {params}):")
                else:
                    lines.append(f"    def __init__(self):")
            else:
                params = _extract_params(method.signature)
                lines.append(f"    def {_safe_name(method.name)}(self{', ' + params if params else ''}):")
            has_body = True
        if not has_body:
            lines.append(f"    pass")
        else:
            lines.append(f"    ...")
        lines.append("")
    return "\n".join(lines)


def _generate_go(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Go type declarations from ReadMenator UML analysis", ""]
    lines.append("package generated")
    lines.append("")
    for node, sym, methods in class_symbols:
        if sym.kind == "struct":
            lines.append(f"type {_safe_name(sym.name)} struct {{ }}")
        elif sym.kind == "interface":
            lines.append(f"type {_safe_name(sym.name)} interface {{")
            for method in methods[:10]:
                lines.append(f"\t{_safe_name(method.name)}()")
            lines.append("}")
        else:
            lines.append(f"type {_safe_name(sym.name)} struct {{")
            lines.append("}")
        for method in methods[:10]:
            if sym.kind == "interface":
                continue
            lines.append(f"func (s *{_safe_name(sym.name)}) {_safe_name(method.name)}() {{ }}")
        lines.append("")
    return "\n".join(lines)


def _generate_rust(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Rust type declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "trait":
            lines.append(f"pub trait {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    fn {_safe_name(method.name)}(&self);")
            lines.append("}")
        elif sym.kind == "enum":
            lines.append(f"pub enum {_safe_name(sym.name)} {{ }}")
        else:
            lines.append(f"pub struct {_safe_name(sym.name)} {{")
            lines.append("}")
            if methods:
                lines.append(f"impl {_safe_name(sym.name)} {{")
                for method in methods[:10]:
                    lines.append(f"    pub fn {_safe_name(method.name)}(&self) {{ }}")
                lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_php(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["<?php", "", "// Generated PHP class declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "interface":
            lines.append(f"interface {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    public function {_safe_name(method.name)}();")
            lines.append("}")
        elif sym.kind == "trait":
            lines.append(f"trait {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    public function {_safe_name(method.name)}() {{ }}")
            lines.append("}")
        else:
            lines.append(f"class {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    public function {_safe_name(method.name)}() {{ }}")
            if not methods:
                lines.append(f"    // No methods extracted")
            lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_kotlin(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Kotlin class declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "interface":
            lines.append(f"interface {_safe_name(sym.name)} {{")
        else:
            lines.append(f"open class {_safe_name(sym.name)} {{")
        for method in methods[:10]:
            lines.append(f"    fun {_safe_name(method.name)}() {{ }}")
        if not methods:
            lines.append(f"    // No methods extracted")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_scala(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Scala class declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "trait":
            lines.append(f"trait {_safe_name(sym.name)} {{")
        elif sym.kind == "class":
            lines.append(f"class {_safe_name(sym.name)} {{")
        else:
            lines.append(f"object {_safe_name(sym.name)} {{")
        for method in methods[:10]:
            lines.append(f"  def {_safe_name(method.name)}(): Unit = {{ }}")
        if not methods:
            lines.append(f"  // No methods extracted")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_swift(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Swift type declarations from ReadMenator UML analysis", ""]
    lines.append("import Foundation")
    lines.append("")
    for node, sym, methods in class_symbols:
        if sym.kind == "protocol":
            lines.append(f"protocol {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    func {_safe_name(method.name)}()")
            lines.append("}")
        elif sym.kind == "enum":
            lines.append(f"enum {_safe_name(sym.name)} {{ }}")
        elif sym.kind == "extension":
            lines.append(f"extension {_safe_name(sym.name)} {{ }}")
        else:
            lines.append(f"class {_safe_name(sym.name)} {{")
            for method in methods[:10]:
                lines.append(f"    func {_safe_name(method.name)}() {{ }}")
            if not methods:
                lines.append(f"    // No methods extracted")
            lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_dart(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["// Generated Dart class declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "interface":
            lines.append(f"abstract class {_safe_name(sym.name)} {{")
        else:
            lines.append(f"class {_safe_name(sym.name)} {{")
        for method in methods[:10]:
            lines.append(f"  void {_safe_name(method.name)}() {{ }}")
        if not methods:
            lines.append(f"  // No methods extracted")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def _generate_ruby(
    class_symbols: List[tuple],
    nodes: List[Node],
    edges: List[Edge],
) -> str:
    lines = ["# Generated Ruby class declarations from ReadMenator UML analysis", ""]
    for node, sym, methods in class_symbols:
        if sym.kind == "module":
            lines.append(f"module {_safe_name(sym.name)}")
        else:
            lines.append(f"class {_safe_name(sym.name)}")
        for method in methods[:10]:
            lines.append(f"  def {_safe_name(method.name)}")
            lines.append(f"  end")
        if not methods:
            lines.append(f"  # No methods extracted")
        lines.append("end")
        lines.append("")
    return "\n".join(lines)


def _safe_name(name: str) -> str:
    return name.replace("-", "_").replace(".", "_").replace(" ", "_")


def _extract_params(signature: str) -> str:
    if not signature:
        return ""
    paren = signature.find("(")
    if paren < 0:
        return ""
    close = signature.find(")")
    if close < 0:
        close = len(signature)
    return signature[paren + 1:close].strip()
