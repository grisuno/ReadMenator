"""Import path resolver for the readmenator knowledge graph.

Maps raw import strings (e.g. ``"os"``, ``"../utils"``, ``"java.util.List"``)
to actual file node IDs within the scanned project so that dependency-
tracing operations work on concrete files rather than opaque strings.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional, Set


class ImportResolver:
    """Resolves raw import strings to project file paths.

    Uses heuristics tuned to each language's import conventions:
    Python dots to slashes, Java dots to directory separators,
    relative-path resolution, and extensionless module detection.
    """

    _PYTHON_STDLIB: Set[str] = {
        "abc", "aifc", "argparse", "array", "ast", "asynchat", "asyncio",
        "asyncore", "atexit", "audioop", "base64", "bdb", "binascii", "binhex",
        "bisect", "builtins", "bz2", "calendar", "cgi", "cgitb", "chunk",
        "cmath", "cmd", "code", "codecs", "codeop", "collections", "colorsys",
        "compileall", "concurrent", "configparser", "contextlib", "contextvars",
        "copy", "copyreg", "cProfile", "crypt", "csv", "ctypes", "curses",
        "dataclasses", "datetime", "dbm", "decimal", "difflib", "dis",
        "distutils", "doctest", "email", "encodings", "enum", "errno",
        "faulthandler", "fcntl", "filecmp", "fileinput", "fnmatch", "formatter",
        "fractions", "ftplib", "functools", "gc", "getopt", "getpass",
        "gettext", "glob", "grp", "gzip", "hashlib", "heapq", "hmac", "html",
        "http", "idlelib", "imaplib", "imghdr", "imp", "importlib", "inspect",
        "io", "ipaddress", "itertools", "json", "keyword", "lib2to3", "linecache",
        "locale", "logging", "lzma", "mailbox", "mailcap", "marshal", "math",
        "mimetypes", "mmap", "modulefinder", "multiprocessing", "netrc", "nis",
        "nntplib", "numbers", "operator", "optparse", "os", "ossaudiodev",
        "parser", "pathlib", "pdb", "pickle", "pickletools", "pipes", "pkgutil",
        "platform", "plistlib", "poplib", "posix", "posixpath", "pprint",
        "profile", "pstats", "pty", "pwd", "py_compile", "pyclbr", "pydoc",
        "queue", "quopri", "random", "re", "readline", "reprlib", "resource",
        "rlcompleter", "runpy", "sched", "secrets", "select", "selectors",
        "shelve", "shlex", "shutil", "signal", "site", "smtpd", "smtplib",
        "sndhdr", "socket", "socketserver", "spwd", "sqlite3", "ssl", "stat",
        "statistics", "string", "stringprep", "struct", "subprocess", "sunau",
        "symbol", "symtable", "sys", "sysconfig", "syslog", "tabnanny",
        "tarfile", "telnetlib", "tempfile", "termios", "test", "textwrap",
        "threading", "time", "timeit", "tkinter", "token", "tokenize",
        "trace", "traceback", "tracemalloc", "tty", "turtle", "turtledemo",
        "types", "typing", "unicodedata", "unittest", "urllib", "uu",
        "uuid", "venv", "warnings", "wave", "weakref", "webbrowser",
        "winreg", "winsound", "wsgiref", "xdrlib", "xml", "xmlrpc",
        "zipapp", "zipfile", "zipimport", "zlib",
    }

    def __init__(self, file_ids: List[str], root: str = "."):
        """Initialise the resolver with all known file paths.

        Args:
            file_ids: List of relative file paths from the scan.
            root: Root directory for relative-path resolution.
        """
        self._file_ids: Set[str] = set(file_ids)
        self._root: str = root
        self._stem_index: Dict[str, List[str]] = self._build_stem_index(file_ids)
        self._dir_index: Dict[str, Set[str]] = self._build_dir_index(file_ids)

    def _build_stem_index(self, file_ids: List[str]) -> Dict[str, List[str]]:
        """Map file stems (without extension) to their full paths."""
        index: Dict[str, List[str]] = {}
        for fid in file_ids:
            stem = Path(fid).stem
            if stem not in index:
                index[stem] = []
            index[stem].append(fid)
        return index

    def _build_dir_index(self, file_ids: List[str]) -> Dict[str, Set[str]]:
        """Map directory paths to the files they contain."""
        index: Dict[str, Set[str]] = {}
        for fid in file_ids:
            parent = str(Path(fid).parent)
            if parent not in index:
                index[parent] = set()
            index[parent].add(fid)
        for key in list(index.keys()):
            parts = key.split("/") if key != "." else []
            for i in range(1, len(parts) + 1):
                prefix = "/".join(parts[:i])
                if prefix not in index:
                    index[prefix] = set()
                index[prefix].update(index[key])
        return index

    def resolve(self, import_str: str, source_file: str = "") -> Optional[str]:
        """Resolve an import string to a concrete project file path.

        Args:
            import_str: The raw import string from the parser.
            source_file: The file that contains the import (for relative resolution).

        Returns:
            Matching file node ID or ``None`` if no match found.
        """
        if not import_str:
            return None

        candidate = self._resolve_relative(import_str, source_file)
        if candidate:
            return candidate

        candidate = self._resolve_extensionless(import_str, source_file)
        if candidate:
            return candidate

        candidate = self._resolve_directory_init(import_str, source_file)
        if candidate:
            return candidate

        candidate = self._resolve_module_dotpath(import_str)
        if candidate:
            return candidate

        candidate = self._resolve_stem_match(import_str)
        if candidate:
            return candidate

        return None

    def resolve_all(self, import_str: str, source_file: str = "") -> List[str]:
        """Resolve *import_str* to all possible matching project file paths.

        Args:
            import_str: The raw import string.
            source_file: The file that contains the import.

        Returns:
            List of matching file node IDs (may be empty).
        """
        results: List[str] = []
        result = self.resolve(import_str, source_file)
        if result:
            results.append(result)
        return results

    def _resolve_relative(self, import_str: str, source_file: str) -> Optional[str]:
        """Resolve a relative import (starts with ``.`` or ``..``)."""
        if not import_str.startswith("."):
            return None
        source_dir = str(Path(source_file).parent) if source_file else ""
        base = Path(source_dir) if source_dir != "." else Path("")
        candidate_path = (base / import_str).as_posix()
        if candidate_path in self._file_ids:
            return candidate_path
        for ext in (".py", ".js", ".ts", ".go", ".rs", ".java", ".cs", ".php", ".dart", ".nim"):
            with_ext = candidate_path + ext
            if with_ext in self._file_ids:
                return with_ext
        init_path = f"{candidate_path}/__init__.py"
        if init_path in self._file_ids:
            return init_path
        return None

    def _resolve_extensionless(self, import_str: str, source_file: str) -> Optional[str]:
        """Resolve a bare module name by appending known extensions."""
        source_dir = str(Path(source_file).parent) if source_file else ""
        for ext in (".py", ".js", ".ts", ".go", ".rs", ".java", ".cs", ".php", ".dart", ".nim"):
            candidate = f"{source_dir}/{import_str}{ext}" if source_dir and source_dir != "." else f"{import_str}{ext}"
            if candidate in self._file_ids:
                return candidate
        return None

    def _resolve_directory_init(self, import_str: str, source_file: str) -> Optional[str]:
        """Resolve as a package directory with __init__ or index file."""
        source_dir = str(Path(source_file).parent) if source_file else ""
        base = f"{source_dir}/{import_str}" if source_dir and source_dir != "." else import_str
        for init_name in ("__init__.py", "index.js", "index.ts", "mod.rs", "lib.rs"):
            candidate = f"{base}/{init_name}"
            if candidate in self._file_ids:
                return candidate
        return None

    def _resolve_module_dotpath(self, import_str: str) -> Optional[str]:
        """Resolve a dotted module path (Python/Java convention)."""
        if "." not in import_str:
            return None
        if import_str.startswith("."):
            return None
        parts = import_str.split(".")
        if any(p in self._PYTHON_STDLIB for p in parts[:1]):
            return None
        candidate_path = "/".join(parts)
        candidates = [
            f"{candidate_path}.py",
            f"{candidate_path}/__init__.py",
            f"{candidate_path}.js",
            f"{candidate_path}/index.js",
            candidate_path,
        ]
        for candidate in candidates:
            if candidate in self._file_ids:
                return candidate
        return None

    def _resolve_stem_match(self, import_str: str) -> Optional[str]:
        """Match by file stem only (last resort)."""
        clean_name = import_str.split("/")[-1].split(".")[-1]
        matches = self._stem_index.get(clean_name, [])
        if len(matches) == 1:
            return matches[0]
        return None
