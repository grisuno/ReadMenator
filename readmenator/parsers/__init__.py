from __future__ import annotations

from typing import Optional

from readmenator._config import Config
from readmenator.parsers._base import LanguageParser
from readmenator.parsers._c import CParser
from readmenator.parsers._python import PythonParser
from readmenator.parsers._go import GoParser
from readmenator.parsers._rust import RustParser
from readmenator.parsers._javascript import JavaScriptParser
from readmenator.parsers._java import JavaParser
from readmenator.parsers._csharp import CSharpParser
from readmenator.parsers._shell import ShellParser
from readmenator.parsers._php import PHPParser
from readmenator.parsers._dart import DartParser
from readmenator.parsers._gdscript import GDScriptParser
from readmenator.parsers._nim import NimParser
from readmenator.parsers._assembly import AssemblyParser
from readmenator.parsers._ruby import RubyParser
from readmenator.parsers._swift import SwiftParser
from readmenator.parsers._kotlin import KotlinParser
from readmenator.parsers._scala import ScalaParser
from readmenator.parsers._lua import LuaParser
from readmenator.parsers._elixir import ElixirParser

_PARSER_MAP = {}

SUPPORTED_EXTENSIONS = []


def _init_parser_map():
    if _PARSER_MAP:
        return
    entries = [
        (".c", CParser), (".cpp", CParser), (".cc", CParser), (".cxx", CParser),
        (".h", CParser), (".hpp", CParser), (".hxx", CParser),
        (".hh", CParser), (".h++", CParser), (".tcc", CParser),
        (".inl", CParser), (".inc", CParser), (".i", CParser),
        (".C", CParser),
        (".py", PythonParser),
        (".go", GoParser),
        (".rs", RustParser),
        (".js", JavaScriptParser), (".ts", JavaScriptParser),
        (".jsx", JavaScriptParser), (".tsx", JavaScriptParser),
        (".java", JavaParser),
        (".cs", CSharpParser),
        (".sh", ShellParser), (".bash", ShellParser), (".zsh", ShellParser),
        (".php", PHPParser),
        (".dart", DartParser),
        (".gd", GDScriptParser),
        (".nim", NimParser),
        (".asm", AssemblyParser), (".s", AssemblyParser), (".S", AssemblyParser),
        (".rb", RubyParser),
        (".swift", SwiftParser),
        (".kt", KotlinParser), (".kts", KotlinParser),
        (".scala", ScalaParser), (".sc", ScalaParser),
        (".lua", LuaParser),
        (".ex", ElixirParser), (".exs", ElixirParser),
    ]
    for ext, cls in entries:
        if ext not in _PARSER_MAP:
            _PARSER_MAP[ext] = cls
        if ext not in SUPPORTED_EXTENSIONS:
            SUPPORTED_EXTENSIONS.append(ext)


def create_parser(extension: str, filename: str, config: Config) -> Optional[LanguageParser]:
    """Factory: return a parser instance for the given file extension."""
    _init_parser_map()
    cls = _PARSER_MAP.get(extension.lower())
    if cls is None:
        return None
    return cls(filename, config)
