#!/usr/bin/env python3
"""
readmenator.py

Production-grade, polyglot, offline codebase knowledge graph generator.
Supports C, C++, Python, Go, Rust, JavaScript, TypeScript, Java, C#, Shell, 
PHP, Dart, GDScript, Nim, Assembly, and more.
Zero dependencies, zero tokens, 100% secure static analysis.

Author: Gris Iscomeback
License: GPL v3
"""
from __future__ import annotations

import ast
import os
import re
import sys
import unittest
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Type


@dataclass(frozen=True)
class Config:
    """Centralized, immutable configuration. No magic numbers or hardcoded paths."""
    ignore_dirs: Tuple[str, ...] = (
        ".git", "__pycache__", "venv", ".venv", "env", ".env", "node_modules", 
        ".tox", ".eggs", ".pytest_cache", "build", "dist", ".idea", ".vscode",
        "target", "bin", "obj", "out", "vendor", "third_party", "deps", 
        "third-party", "thirdparty", ".m2", ".gradle", ".nuget", "packages", 
        "Pods", ".dart_tool", ".pub-cache", "bower_components", ".yarn", 
        "Carthage", "node_packages", ".meteor"
    )
    output_graph_file: str = "KNOWLEDGE_BASE.md"
    max_file_size_mb: float = 10.0
    max_directory_depth: int = 20
    docstring_lookback_lines: int = 15
    docstring_max_length: int = 150
    mermaid_max_nodes: int = 300
    mermaid_module_style: str = "fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff"
    mermaid_class_style: str = "fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff"
    mermaid_function_style: str = "fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa"
    mermaid_external_style: str = "fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa"


@dataclass
class Symbol:
    """Represents a code symbol (function, class, struct, etc.)."""
    name: str
    type: str
    line: int
    doc: str = ""
    signature: str = ""


@dataclass
class Node:
    """Represents a file/module in the codebase knowledge graph."""
    id: str
    label: str
    type: str
    language: str
    doc: str
    symbols: List[Symbol] = field(default_factory=list)


@dataclass
class Edge:
    """Represents a relationship between two nodes."""
    source: str
    target: str
    relation: str


class LanguageParser:
    """Base class for language-specific parsers (Strategy Pattern)."""
    
    def __init__(self, filename: str, config: Config) -> None:
        """Initialize parser with filename and configuration."""
        self.filename = filename
        self.config = config
        self.symbols: List[Symbol] = []
        self.imports: List[str] = []
        self.lines: List[str] = []

    def parse(self, content: str) -> None:
        """Parse the file content and extract symbols and imports."""
        self.lines = content.split('\n')
        self._extract_specifics(content)

    def _extract_specifics(self, content: str) -> None:
        """Override in subclasses to implement language-specific extraction."""
        raise NotImplementedError

    def _extract_docstring(self, line_num: int) -> str:
        """Extract documentation comment preceding a symbol."""
        if line_num >= len(self.lines):
            return ""
        
        doc_lines = []
        in_block_comment = False
        
        for i in range(line_num - 1, max(-1, line_num - self.config.docstring_lookback_lines), -1):
            line = self.lines[i].strip()
            
            if line.endswith('*/'):
                in_block_comment = True
                doc_lines.insert(0, line.rstrip('*/').strip())
                continue
            if in_block_comment:
                doc_lines.insert(0, line.lstrip('/*').lstrip('*').strip())
                if line.startswith('/*') or line.startswith('/**'):
                    break
                continue
            
            if line.startswith('///') or line.startswith('//!'):
                doc_lines.insert(0, line[3:].strip())
            elif line.startswith('//'):
                doc_lines.insert(0, line[2:].strip())
            elif line.startswith('#') and not line.startswith('#!'):
                doc_lines.insert(0, line[1:].strip())
            elif line == '':
                continue
            else:
                break
        
        doc = ' '.join(doc_lines).strip()
        doc = re.sub(r'^[\-\*\+]\s*', '', doc)
        if len(doc) > self.config.docstring_max_length:
            doc = doc[:self.config.docstring_max_length - 3] + "..."
        return doc


class CParser(LanguageParser):
    """Parser for C and C++ files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract C/C++ specific symbols and imports."""
        for match in re.finditer(r'^\s*#\s*include\s*[<"]([^>"]+)[>"]', content, re.MULTILINE):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'\b(?:typedef\s+)?struct\s+(\w+)\s*(?:\{|;)', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='struct', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'\bclass\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+(\w+))?\s*\{', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        func_pattern = r'^[\w\s\*&:<>]+?\b([a-zA-Z_]\w*)\s*\([^;{]*\)\s*(?:const)?\s*(?:override)?\s*\{'
        for match in re.finditer(func_pattern, content, re.MULTILINE):
            name = match.group(1)
            if name in ['if', 'for', 'while', 'switch', 'catch', 'return', 'sizeof', 'typedef']:
                continue
            
            preceding_text = content[max(0, match.start()-200):match.start()]
            if '/*' in preceding_text and '*/' not in preceding_text.split('/*')[-1]:
                continue
                
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=name, type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num),
                signature=match.group(0).strip()[:80]
            ))
        
        for match in re.finditer(r'^\s*#\s*define\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='macro', line=line_num + 1
            ))


class PythonParser(LanguageParser):
    """Parser for Python files using the native ast module for 100% accuracy."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Python specific symbols and imports with warning suppression."""
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', SyntaxWarning)
            warnings.simplefilter('ignore', DeprecationWarning)
            try:
                tree = ast.parse(content, filename=self.filename)
            except SyntaxError:
                return

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.imports.append(alias.name)
                else:
                    if node.module:
                        self.imports.append(node.module)
            
            elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                self.symbols.append(Symbol(
                    name=node.name, type='function', line=node.lineno,
                    doc=ast.get_docstring(node) or "",
                    signature=f"def {node.name}(...)"
                ))
            
            elif isinstance(node, ast.ClassDef):
                self.symbols.append(Symbol(
                    name=node.name, type='class', line=node.lineno,
                    doc=ast.get_docstring(node) or ""
                ))


class GoParser(LanguageParser):
    """Parser for Go files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Go specific symbols and imports."""
        import_block = re.search(r'import\s*\((.*?)\)', content, re.DOTALL)
        if import_block:
            for match in re.finditer(r'"([^"]+)"', import_block.group(1)):
                self.imports.append(match.group(1))
        else:
            for match in re.finditer(r'import\s+"([^"]+)"', content):
                self.imports.append(match.group(1))
        
        for match in re.finditer(r'^func\s+(?:\([^)]+\)\s+)?(\w+)\s*\(', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'^type\s+(\w+)\s+(struct|interface)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type=match.group(2), line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class RustParser(LanguageParser):
    """Parser for Rust files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Rust specific symbols and imports."""
        for match in re.finditer(r'^use\s+([\w:]+)', content, re.MULTILINE):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'^(?:pub\s+)?(?:async\s+)?fn\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'^(?:pub\s+)?struct\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='struct', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'^(?:pub\s+)?trait\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='trait', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'^(?:pub\s+)?enum\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='enum', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class JavaScriptParser(LanguageParser):
    """Parser for JavaScript and TypeScript files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract JS/TS specific symbols and imports."""
        for match in re.finditer(r'(?:import|require)\s*\(?[\'"]([^\'"]+)[\'"]\)?', content):
            self.imports.append(match.group(1))
        
        patterns = [
            r'(?:^|\s)function\s+(\w+)',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(',
            r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?function',
        ]
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                name = match.group(1)
                if name not in ['if', 'for', 'while', 'switch', 'catch']:
                    line_num = content[:match.start()].count('\n')
                    self.symbols.append(Symbol(
                        name=name, type='function', line=line_num + 1,
                        doc=self._extract_docstring(line_num)
                    ))
        
        for match in re.finditer(r'class\s+(\w+)(?:\s+extends\s+(\w+))?', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class JavaParser(LanguageParser):
    """Parser for Java files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Java specific symbols and imports."""
        for match in re.finditer(r'^import\s+([\w.]+)', content, re.MULTILINE):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'(?:public|private|protected)?\s*(?:abstract\s+)?(?:class|interface)\s+(\w+)', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        method_pattern = r'(?:public|private|protected)?\s*(?:static\s+)?(?:[\w<>\[\]]+\s+)+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{'
        for match in re.finditer(method_pattern, content):
            name = match.group(1)
            if name not in ['if', 'for', 'while', 'switch', 'catch']:
                line_num = content[:match.start()].count('\n')
                self.symbols.append(Symbol(
                    name=name, type='method', line=line_num + 1,
                    doc=self._extract_docstring(line_num)
                ))


class CSharpParser(LanguageParser):
    """Parser for C# files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract C# specific symbols and imports."""
        for match in re.finditer(r'^using\s+([\w.]+)', content, re.MULTILINE):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'(?:public|private|protected|internal)?\s*(?:static\s+)?(?:class|struct|interface|record)\s+(\w+)', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        method_pattern = r'(?:public|private|protected|internal)?\s*(?:static\s+)?(?:virtual\s+)?(?:override\s+)?(?:async\s+)?(?:[\w<>\[\]]+\s+)+(\w+)\s*\([^)]*\)\s*\{'
        for match in re.finditer(method_pattern, content):
            name = match.group(1)
            if name not in ['if', 'for', 'while', 'switch', 'catch']:
                line_num = content[:match.start()].count('\n')
                self.symbols.append(Symbol(
                    name=name, type='method', line=line_num + 1,
                    doc=self._extract_docstring(line_num)
                ))


class ShellParser(LanguageParser):
    """Parser for Shell/Bash/Zsh files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Shell specific symbols."""
        patterns = [
            r'^(\w+)\s*\(\)\s*\{',
            r'^function\s+(\w+)\s*(?:\(\))?\s*\{',
        ]
        for pattern in patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                line_num = content[:match.start()].count('\n')
                self.symbols.append(Symbol(
                    name=match.group(1), type='function', line=line_num + 1,
                    doc=self._extract_docstring(line_num)
                ))


class PHPParser(LanguageParser):
    """Parser for PHP files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract PHP specific symbols and imports."""
        for match in re.finditer(r'(?:use|require|include)(?:_once)?\s+[\'"]?([^\'";\s]+)', content):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'function\s+(\w+)\s*\(', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'class\s+(\w+)', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class DartParser(LanguageParser):
    """Parser for Dart/Flutter files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Dart specific symbols and imports."""
        for match in re.finditer(r'import\s+[\'"]([^\'"]+)[\'"]', content):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'class\s+(\w+)(?:\s+extends\s+(\w+))?', content):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='class', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'(?:void|int|String|bool|dynamic|Future|[\w<>]+)\s+(\w+)\s*\(', content):
            name = match.group(1)
            if name not in ['if', 'for', 'while', 'switch']:
                line_num = content[:match.start()].count('\n')
                self.symbols.append(Symbol(
                    name=name, type='function', line=line_num + 1,
                    doc=self._extract_docstring(line_num)
                ))


class GDScriptParser(LanguageParser):
    """Parser for Godot GDScript files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract GDScript specific symbols and imports."""
        for match in re.finditer(r'^(?:extends|class_name)\s+(\w+)', content, re.MULTILINE):
            self.imports.append(match.group(1))
        
        for match in re.finditer(r'^func\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class NimParser(LanguageParser):
    """Parser for Nim files."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Nim specific symbols and imports."""
        for match in re.finditer(r'^import\s+([\w,/ ]+)', content, re.MULTILINE):
            self.imports.extend([x.strip() for x in match.group(1).split(',')])
        
        for match in re.finditer(r'^(?:proc|func|method)\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))
        
        for match in re.finditer(r'^type\s+(\w+)', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='struct', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class AssemblyParser(LanguageParser):
    """Parser for Assembly files (.asm, .s)."""
    
    def _extract_specifics(self, content: str) -> None:
        """Extract Assembly specific symbols."""
        for match in re.finditer(r'^([a-zA-Z_]\w*):', content, re.MULTILINE):
            line_num = content[:match.start()].count('\n')
            self.symbols.append(Symbol(
                name=match.group(1), type='function', line=line_num + 1,
                doc=self._extract_docstring(line_num)
            ))


class ParserFactory:
    """Factory to instantiate the correct parser based on file extension."""
    
    _parsers: Dict[str, Type[LanguageParser]] = {
        '.c': CParser, '.cpp': CParser, '.cc': CParser, '.cxx': CParser,
        '.h': CParser, '.hpp': CParser, '.hxx': CParser,
        '.py': PythonParser,
        '.go': GoParser,
        '.rs': RustParser,
        '.js': JavaScriptParser, '.ts': JavaScriptParser, 
        '.jsx': JavaScriptParser, '.tsx': JavaScriptParser,
        '.java': JavaParser,
        '.cs': CSharpParser,
        '.sh': ShellParser, '.bash': ShellParser, '.zsh': ShellParser,
        '.php': PHPParser,
        '.dart': DartParser,
        '.gd': GDScriptParser,
        '.nim': NimParser,
        '.asm': AssemblyParser, '.s': AssemblyParser, '.S': AssemblyParser,
    }

    @classmethod
    def get_parser(cls, extension: str, filename: str, config: Config) -> Optional[LanguageParser]:
        """Return the appropriate parser instance for the given file extension."""
        parser_class = cls._parsers.get(extension.lower())
        if parser_class:
            return parser_class(filename, config)
        return None


class PolyglotScanner:
    """Securely walks directory trees and orchestrates polyglot AST/Regex analysis."""

    def __init__(self, config: Config) -> None:
        """Initialize scanner with configuration."""
        self._config = config

    def _is_ignored(self, path: Path) -> bool:
        """Check if path contains ignored directories."""
        return any(part in self._config.ignore_dirs for part in path.parts)

    def _validate_path_security(self, path: Path) -> bool:
        """Validate path is safe to process."""
        try:
            if path.is_symlink():
                return False
            if path.is_file():
                size_mb = path.stat().st_size / (1024.0 * 1024.0)
                if size_mb > self._config.max_file_size_mb:
                    return False
            return True
        except OSError:
            return False

    def _check_directory_depth(self, path: Path, root: Path) -> bool:
        """Ensure directory depth doesn't exceed limit."""
        try:
            rel_path = path.relative_to(root)
            return len(rel_path.parts) <= self._config.max_directory_depth
        except ValueError:
            return False

    def scan(self, root: Path) -> Tuple[List[Node], List[Edge]]:
        """Scan codebase and return nodes and edges."""
        all_nodes: List[Node] = []
        all_edges: List[Edge] = []

        if not root.is_dir():
            raise ValueError(f"Path is not a valid directory: {root}")

        root = root.resolve()

        for file_path in sorted(root.rglob('*')):
            if not file_path.is_file():
                continue

            if not self._validate_path_security(file_path):
                continue

            rel_path = file_path.relative_to(root)
            if self._is_ignored(rel_path):
                continue

            if not self._check_directory_depth(file_path, root):
                continue

            rel_path_str = rel_path.as_posix()
            extension = file_path.suffix

            parser = ParserFactory.get_parser(extension, rel_path_str, self._config)
            if not parser:
                continue

            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                parser.parse(content)

                node = Node(
                    id=rel_path_str,
                    label=file_path.name,
                    type='module',
                    language=extension.lstrip('.'),
                    doc='',
                    symbols=parser.symbols
                )
                all_nodes.append(node)

                for imp in parser.imports:
                    all_edges.append(Edge(source=rel_path_str, target=imp, relation='imports'))

            except Exception:
                continue

        return all_nodes, all_edges


class MermaidRenderer:
    """Converts graph primitives into Mermaid diagram syntax."""

    def __init__(self, config: Config) -> None:
        """Initialize renderer with configuration."""
        self._config = config

    def _sanitize_id(self, node_id: str) -> str:
        """Sanitize node ID for Mermaid compatibility."""
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', node_id)
        if sanitized and sanitized[0].isdigit():
            sanitized = 'n_' + sanitized
        return sanitized

    def render(self, nodes: List[Node], edges: List[Edge]) -> Tuple[str, bool]:
        """Render complete Mermaid graph with intelligent pruning."""
        lines = ["graph TD"]
        lines.append(f"    classDef mod {self._config.mermaid_module_style};")
        lines.append(f"    classDef cls {self._config.mermaid_class_style};")
        lines.append(f"    classDef fn {self._config.mermaid_function_style};")
        lines.append(f"    classDef ext {self._config.mermaid_external_style};")

        seen_ids: Set[str] = set()
        node_count = 0
        is_truncated = False

        node_import_counts = {node.id: 0 for node in nodes}
        for edge in edges:
            if edge.source in node_import_counts:
                node_import_counts[edge.source] += 1

        sorted_nodes = sorted(
            nodes, 
            key=lambda n: (node_import_counts.get(n.id, 0), len(n.symbols)), 
            reverse=True
        )

        for node in sorted_nodes:
            safe_id = self._sanitize_id(node.id)
            if safe_id not in seen_ids:
                label = node.label.replace('"', '\\"')
                lines.append(f'    {safe_id}["{label} ({node.language})"]')
                lines.append(f"    class {safe_id} mod;")
                seen_ids.add(safe_id)
                node_count += 1

                for symbol in node.symbols[:5]:
                    if node_count >= self._config.mermaid_max_nodes:
                        is_truncated = True
                        break
                        
                    symbol_id = f"{safe_id}_{self._sanitize_id(symbol.name)}"
                    symbol_label = symbol.name.replace('"', '\\"')
                    lines.append(f'    {symbol_id}["{symbol_label}"]')
                    
                    if symbol.type in ['class', 'struct', 'interface', 'trait', 'enum']:
                        lines.append(f"    class {symbol_id} cls;")
                    else:
                        lines.append(f"    class {symbol_id} fn;")
                    
                    lines.append(f"    {safe_id} --> {symbol_id}")
                    node_count += 1
            
            if node_count >= self._config.mermaid_max_nodes:
                is_truncated = True
                break

        for edge in edges:
            if is_truncated:
                break
            src = self._sanitize_id(edge.source)
            if src in seen_ids:
                target_id = self._sanitize_id(f"ext_{edge.target}")
                target_label = edge.target.split('/')[-1].replace('"', '\\"')
                
                if target_id not in seen_ids:
                    if node_count >= self._config.mermaid_max_nodes:
                        is_truncated = True
                        break
                    lines.append(f'    {target_id}["{target_label}"]')
                    lines.append(f"    class {target_id} ext;")
                    seen_ids.add(target_id)
                    node_count += 1
                
                lines.append(f"    {src} -.->|imports| {target_id}")

        return "\n".join(lines), is_truncated


class DocumentationGenerator:
    """Generates comprehensive Markdown documentation."""

    def __init__(self, config: Config) -> None:
        """Initialize generator with configuration."""
        self._config = config
        self._mermaid = MermaidRenderer(config)

    def generate(self, nodes: List[Node], edges: List[Edge]) -> str:
        """Generate complete knowledge base document."""
        total_symbols = sum(len(n.symbols) for n in nodes)
        graph_output, is_truncated = self._mermaid.render(nodes, edges)
        
        sections = [
            "# Polyglot Codebase Knowledge Graph",
            "",
            "> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.",
            "> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator) ",
            "",
            f"**Total Files Parsed:** {len(nodes)} | **Total Symbols Extracted:** {total_symbols} | **Total Imports:** {len(edges)}",
            "",
            "## Structural Knowledge Map",
        ]
        
        if is_truncated:
            sections.append(f"> **Note:** The visual graph below has been intelligently pruned to the top {self._config.mermaid_max_nodes} most relevant nodes to prevent rendering crashes. Full details of all {len(nodes)} files are documented below.")
            sections.append("")

        sections.extend([
            "```mermaid",
            graph_output,
            "```",
            "",
            "---",
            "",
            "## Architecture Reference",
            "",
        ])

        files_by_lang: Dict[str, List[Node]] = {}
        for node in nodes:
            lang = node.language.upper() if node.language else "UNKNOWN"
            if lang not in files_by_lang:
                files_by_lang[lang] = []
            files_by_lang[lang].append(node)

        for lang, lang_nodes in sorted(files_by_lang.items()):
            sections.append(f"### {lang} ({len(lang_nodes)} files)")
            sections.append("")

            for node in lang_nodes:
                sections.append(f"#### `{node.label}`")
                sections.append(f"**Path:** `{node.id}`")
                sections.append("")

                if node.symbols:
                    symbols_by_type: Dict[str, List[Symbol]] = {}
                    for symbol in node.symbols:
                        if symbol.type not in symbols_by_type:
                            symbols_by_type[symbol.type] = []
                        symbols_by_type[symbol.type].append(symbol)

                    for sym_type, symbols in sorted(symbols_by_type.items()):
                        sections.append(f"**{sym_type.title()}s:**")
                        for symbol in symbols:
                            doc_str = f" - *{symbol.doc}*" if symbol.doc else ""
                            sections.append(f"- `{symbol.name}` (line {symbol.line}){doc_str}")
                        sections.append("")
                else:
                    sections.append("*No symbols extracted*")
                    sections.append("")

        return "\n".join(sections)


class readmenatorApplication:
    """Main application orchestrator."""

    def __init__(self, config: Optional[Config] = None) -> None:
        """Initialize application with optional configuration."""
        self._config = config or Config()
        self._scanner = PolyglotScanner(self._config)
        self._generator = DocumentationGenerator(self._config)

    def run(self, target_dir: str) -> None:
        """Execute documentation generation."""
        root = Path(target_dir).resolve()
        nodes, edges = self._scanner.scan(root)
        content = self._generator.generate(nodes, edges)

        output_path = root / self._config.output_graph_file
        output_path.write_text(content, encoding='utf-8')
        print(f"[+] Knowledge base generated: {output_path}")
        print(f"[+] Files: {len(nodes)} | Symbols: {sum(len(n.symbols) for n in nodes)} | Imports: {len(edges)}")


class TestPolyglotreadmenator(unittest.TestCase):
    """Comprehensive test suite validating polyglot contracts."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.config = Config()
        self.test_dir = Path("__readmenator_polyglot_fixture__")
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self) -> None:
        """Tear down test fixtures."""
        import shutil
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def _write_fixture(self, name: str, content: str) -> None:
        """Write test fixture to disk."""
        path = self.test_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def test_c_parser(self) -> None:
        """Validate C parser extraction logic."""
        self._write_fixture("test.c", """
#include <stdio.h>
/** Adds two numbers */
int add(int a, int b) {
    return a + b;
}
struct Point { int x; int y; };
""")
        scanner = PolyglotScanner(self.config)
        nodes, edges = scanner.scan(self.test_dir)
        
        symbols = nodes[0].symbols
        names = [s.name for s in symbols]
        self.assertIn("add", names)
        self.assertIn("Point", names)
        self.assertTrue(any(e.target == "stdio.h" for e in edges))

    def test_env_and_vendor_dirs_ignored(self) -> None:
        """BDD: Given vendor/env dirs, When scanned, Then they are ignored."""
        self._write_fixture("env/lib/x.py", "def fake(): pass")
        self._write_fixture("vendor/x.py", "def fake(): pass")
        self._write_fixture("node_modules/x.js", "function fake() {}")
        self._write_fixture("main.py", "def real(): pass")
        
        scanner = PolyglotScanner(self.config)
        nodes, _ = scanner.scan(self.test_dir)
        
        paths = [n.id for n in nodes]
        self.assertIn("main.py", paths)
        self.assertNotIn("env/lib/x.py", paths)
        self.assertNotIn("vendor/x.py", paths)
        self.assertNotIn("node_modules/x.js", paths)

    def test_syntax_warnings_suppressed(self) -> None:
        """Security: Invalid escape sequences in Python strings must not emit warnings."""
        self._write_fixture("regex_heavy.py", r'pattern = "\e \. \S"')
        
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            scanner = PolyglotScanner(self.config)
            scanner.scan(self.test_dir)
            
            syntax_warnings = [x for x in w if issubclass(x.category, SyntaxWarning)]
            self.assertEqual(len(syntax_warnings), 0, "SyntaxWarning leaked to stdout")

    def test_mermaid_graph_truncation(self) -> None:
        """Resilience: Mermaid renderer prunes graph if node limit is exceeded."""
        small_config = Config(mermaid_max_nodes=5)
        nodes = [Node(id=f"f{i}.py", label=f"f{i}.py", type="module", language="py", doc="") for i in range(20)]
        renderer = MermaidRenderer(small_config)
        output, is_truncated = renderer.render(nodes, [])
        
        self.assertTrue(is_truncated)
        self.assertTrue(output.count("classDef mod") == 1)
        self.assertLessEqual(output.count('class '), small_config.mermaid_max_nodes + 10)

    def test_polyglot_integration(self) -> None:
        """Validate full polyglot integration."""
        self._write_fixture("main.c", "int main() { return 0; }")
        self._write_fixture("utils.py", "def helper(): pass")
        self._write_fixture("server.go", "func main() {}")
        self._write_fixture("lib.rs", "fn calculate() {}")
        
        scanner = PolyglotScanner(self.config)
        nodes, edges = scanner.scan(self.test_dir)
        
        self.assertEqual(len(nodes), 4)
        total_symbols = sum(len(n.symbols) for n in nodes)
        self.assertTrue(total_symbols >= 4)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.argv = [sys.argv[0]]
        unittest.main(verbosity=2)
    elif len(sys.argv) == 2:
        readmenatorApplication().run(sys.argv[1])
    else:
        print("Usage:")
        print("  Generate docs:  python readmenator.py /path/to/project")
        print("  Run tests:      python readmenator.py --test")
        print("")
        print("Supported languages:")
        print("  C/C++ (.c, .cpp, .h, .hpp)")
        print("  Python (.py)")
        print("  Go (.go)")
        print("  Rust (.rs)")
        print("  JavaScript/TypeScript (.js, .ts, .jsx, .tsx)")
        print("  Java (.java)")
        print("  C# (.cs)")
        print("  Shell (.sh, .bash, .zsh)")
        print("  PHP (.php)")
        print("  Dart (.dart)")
        print("  GDScript (.gd)")
        print("  Nim (.nim)")
        print("  Assembly (.asm, .s)")
        sys.exit(1)
