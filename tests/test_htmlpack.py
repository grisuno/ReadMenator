"""Contract tests for embedded page payload compression (readmenator/_htmlpack.py)."""

from __future__ import annotations

import base64
import gzip
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import Dict

from readmenator._app import readmenatorApplication
from readmenator._config import Config
from readmenator._htmlpack import (
    PAYLOAD_ENCODING_GZIP,
    PAYLOAD_LOADER_JS,
    compress_text,
    escape_json_for_script,
    payload_script,
    read_payload_script,
    should_compress,
)

PAGE_PAYLOADS = {
    "readmenator-apidocs/index.html": ["api-data"],
    "readmenator-apidocs/flows.html": ["fv-data"],
    "readmenator-maps/flows.html": ["fv-data"],
    "readmenator-maps/graph-force.html": ["fg-data", "fg-analytics"],
    "readmenator-maps/graph-bundle.html": ["bundle-data"],
    "readmenator-maps/architecture.html": ["vis-nodes", "vis-edges", "vis-views", "vis-meta", "vis-physics", "vis-roles"],
    "offline-architecture.html": ["map-nodes", "map-edges", "map-views", "map-meta"],
}

PROJECT_FILES = {
    "pkg/__init__.py": '"""Demo package."""\n',
    "pkg/core.py": '"""Core logic."""\nfrom pkg.util import helper\n\n\nclass Engine:\n    """Runs things."""\n\n    def run(self, x: int) -> int:\n        """Run once."""\n        return helper(x)\n',
    "pkg/util.py": '"""Helpers."""\n\n\ndef helper(x: int) -> int:\n    """Double </script> x."""\n    return x * 2\n',
    "pkg/__main__.py": '"""Entry."""\nfrom pkg.core import Engine\n\n\ndef main() -> None:\n    """Start."""\n    Engine().run(1)\n\n\nif __name__ == "__main__":\n    main()\n',
}


def _inline_scripts(document: str) -> list:
    """Return the bodies of executable inline script elements."""
    return [m.group(1) for m in re.finditer(r"<script>(.*?)</script>", document, re.S)]


def _build_site(root: Path, config: Config) -> Dict[str, str]:
    """Write a tiny project, export API docs, maps, and an offline map; return page texts."""
    for rel, text in PROJECT_FILES.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    app = readmenatorApplication(config)
    app.export_apidocs(str(root))
    app.export_diagrams(str(root), full=True)
    factory = app._factory
    nodes, edges = factory.scanner.scan(root)
    maps = factory.diagram_builder.build_all(nodes, edges, full=True)
    (root / "offline-architecture.html").write_text(factory.diagram_renderer.render(maps["architecture"]), encoding="utf-8")
    return {rel: (root / rel).read_text(encoding="utf-8") for rel in PAGE_PAYLOADS}


class TestPayloadScriptContract(unittest.TestCase):
    """Contract: plain below the threshold, deterministic gzip+base64 above it."""

    def setUp(self) -> None:
        """Prepare configurations."""
        self.config = Config()
        self.always = replace(self.config, PAYLOAD_COMPRESSION_MIN_BYTES=0)
        self.payload = {"doc": "</script><script>alert(1)</script> & more", "n": [1, 2, 3]}

    def test_htmlpack_small_payload_stays_plain_and_escaped(self) -> None:
        tag = payload_script("x-data", self.payload, self.config)
        self.assertTrue(tag.startswith('<script type="application/json" id="x-data">'))
        self.assertNotIn("</script><script>", tag)
        self.assertEqual(read_payload_script(tag, "x-data"), self.payload)

    def test_htmlpack_large_payload_is_gzip_base64_and_round_trips(self) -> None:
        tag = payload_script("x-data", self.payload, self.always)
        self.assertIn(f'data-encoding="{PAYLOAD_ENCODING_GZIP}"', tag)
        body = re.search(r">([A-Za-z0-9+/=]+)</script>$", tag).group(1)
        self.assertEqual(json.loads(gzip.decompress(base64.b64decode(body))), self.payload)
        self.assertEqual(read_payload_script(tag, "x-data"), self.payload)

    def test_htmlpack_compression_is_deterministic(self) -> None:
        self.assertEqual(payload_script("x", self.payload, self.always), payload_script("x", self.payload, self.always))
        self.assertEqual(compress_text("abc", self.config), compress_text("abc", self.config))
        self.assertEqual(base64.b64decode(compress_text("abc", self.config))[4:8], b"\x00\x00\x00\x00")

    def test_htmlpack_threshold_and_disable_flag(self) -> None:
        limit = self.config.PAYLOAD_COMPRESSION_MIN_BYTES
        self.assertFalse(should_compress(limit - 1, self.config))
        self.assertTrue(should_compress(limit, self.config))
        self.assertFalse(should_compress(limit * 4, replace(self.config, PAYLOAD_COMPRESSION_ENABLED=False)))

    def test_htmlpack_plain_format_matches_legacy_serialization(self) -> None:
        tag = payload_script("x", {"a": "<b>&"}, self.config, compact=False, escape="<")
        self.assertIn('{"a": "\\u003cb>&"}', tag)
        self.assertIn('{"a":"\\u003cb\\u003e\\u0026"}', payload_script("x", {"a": "<b>&"}, self.config))
        self.assertEqual(escape_json_for_script("<>&", ">"), "\\u003c\\u003e&")

    def test_htmlpack_missing_or_empty_element_reads_none(self) -> None:
        self.assertIsNone(read_payload_script("<p></p>", "x"))
        self.assertIsNone(read_payload_script('<script type="application/json" id="x"></script>', "x"))

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_htmlpack_browser_loader_decodes_both_encodings(self) -> None:
        packed = payload_script("x", self.payload, self.always)
        plain = payload_script("x", self.payload, self.config)
        script = (
            "const tags=" + json.dumps({"packed": packed, "plain": plain}) + ";\n"
            "if(typeof DecompressionStream==='undefined'){console.log('SKIP');process.exit(0);}\n"
            "let current='';\n"
            "global.document={getElementById:()=>{const m=current.match(/<script([^>]*)>([^<]*)<\\/script>$/)||"
            "current.match(/<script([^>]*)>(.*)<\\/script>$/s);"
            "return {textContent:m[2],getAttribute:k=>{const a=m[1].match(new RegExp(k+'=\"([^\"]+)\"'));return a?a[1]:null;}};}};\n"
            + PAYLOAD_LOADER_JS + "\n"
            "(async()=>{const out={};for(const k of ['packed','plain']){current=tags[k];out[k]=await readmenatorPayload('x',null);}"
            "current='<script type=\"application/json\" id=\"x\"></script>';out.empty=await readmenatorPayload('x',{d:1});"
            "console.log(JSON.stringify(out));})();\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "loader.js"
            path.write_text(script, encoding="utf-8")
            result = subprocess.run(["node", str(path)], capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        if result.stdout.strip() == "SKIP":
            self.skipTest("node lacks DecompressionStream")
        out = json.loads(result.stdout)
        self.assertEqual(out["packed"], self.payload)
        self.assertEqual(out["plain"], self.payload)
        self.assertEqual(out["empty"], {"d": 1})


class TestCompressedPagesContract(unittest.TestCase):
    """Contract: every data-heavy page decodes the same payload whether plain or compressed."""

    @classmethod
    def setUpClass(cls) -> None:
        """Build the same tiny project twice: compression off and forced on."""
        base = replace(Config(), VIDEO_ENABLED=False, GH_WIKI_ENABLED=False)
        cls.tmp = Path(tempfile.mkdtemp())
        cls.plain = _build_site(cls.tmp / "plain" / "demo", replace(base, PAYLOAD_COMPRESSION_ENABLED=False))
        cls.packed = _build_site(cls.tmp / "packed" / "demo", replace(base, PAYLOAD_COMPRESSION_MIN_BYTES=0))

    @classmethod
    def tearDownClass(cls) -> None:
        """Remove the temporary projects."""
        shutil.rmtree(cls.tmp)

    def test_htmlpack_pages_compress_every_payload_when_forced(self) -> None:
        for page, ids in PAGE_PAYLOADS.items():
            for element in ids:
                self.assertRegex(self.packed[page], r'id="' + element + r'" data-encoding="gzip\+base64">', page)
                self.assertIn('id="' + element + '">', self.plain[page], page)

    def test_htmlpack_pages_decode_identical_payloads(self) -> None:
        for page, ids in PAGE_PAYLOADS.items():
            for element in ids:
                plain = read_payload_script(self.plain[page], element)
                self.assertIsNotNone(plain, f"{page} {element}")
                self.assertEqual(plain, read_payload_script(self.packed[page], element), f"{page} {element}")

    def test_htmlpack_pages_boot_through_the_shared_loader(self) -> None:
        for page, document in self.packed.items():
            self.assertEqual(document.count("function readmenatorPayload("), 1, page)
            self.assertIn("readmenatorPayloadError", document, page)
            self.assertNotRegex(document, r"const (RAW|DATA)=\{", page)
            self.assertNotIn("</script><script>alert", document, page)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_htmlpack_pages_inline_scripts_are_valid_javascript(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for page, document in self.packed.items():
                for index, body in enumerate(_inline_scripts(document)):
                    path = Path(tmp) / f"{index}.js"
                    path.write_text(body, encoding="utf-8")
                    result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True, timeout=60)
                    self.assertEqual(result.returncode, 0, f"{page} script {index}: {result.stderr}")


if __name__ == "__main__":
    unittest.main()
