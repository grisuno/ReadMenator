"""Compact JSON payload embedding for self-contained HTML pages.

Large pages embed their data as one JSON document. Generated API data
is highly repetitive (file paths, kinds, signatures, parameter names),
so payloads above PAYLOAD_COMPRESSION_MIN_BYTES are gzip-compressed and
base64-encoded into the script tag. The page decodes them offline with
the browser's native DecompressionStream: zero dependencies, zero
requests, and it works from file:// as well as static hosting.
Small payloads stay plain JSON so they remain greppable.
"""

from __future__ import annotations

import base64
import gzip
import html
import json
import re
from typing import Mapping, Optional

from readmenator._config import Config


PAYLOAD_ENCODING_GZIP = "gzip+base64"

PAYLOAD_LOADER_JS = r"""function readmenatorPayload(id,fallback){
  var el=document.getElementById(id),text=el?el.textContent:"";
  if(!text||!text.trim())return Promise.resolve(fallback===undefined?null:fallback);
  if(el.getAttribute("data-encoding")!=="gzip+base64")return Promise.resolve(JSON.parse(text));
  if(typeof DecompressionStream==="undefined")return Promise.reject(new Error("This browser cannot decompress the embedded data (DecompressionStream missing). Open the page in a current Chrome, Edge, Firefox or Safari."));
  var bin=atob(text.replace(/\s+/g,"")),bytes=new Uint8Array(bin.length);
  for(var i=0;i<bin.length;i++)bytes[i]=bin.charCodeAt(i);
  return new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"))).text().then(JSON.parse);
}
function readmenatorPayloads(specs){
  return Promise.all(specs.map(function(spec){return readmenatorPayload(spec[0],spec[1]);}));
}
function readmenatorPayloadError(err){
  var box=document.createElement("pre");box.setAttribute("role","alert");
  box.style.cssText="position:relative;z-index:9999;margin:24px;padding:16px;border:1px solid #f87171;border-radius:8px;background:#1f1115;color:#fecaca;white-space:pre-wrap";
  box.textContent="Could not load the embedded data: "+(err&&err.message?err.message:String(err));
  document.body.insertBefore(box,document.body.firstChild);
}"""


_UNICODE_ESCAPES = {"<": "\\u003c", ">": "\\u003e", "&": "\\u0026"}


def escape_json_for_script(text: str, chars: str = "<>&") -> str:
    """Escape JSON text so it can never close or confuse a script element.

    Args:
        text: Serialized JSON.
        chars: Characters to unicode-escape; "<" is always included.

    Returns:
        JSON text with the requested characters unicode-escaped.
    """
    for char in "<" + chars.replace("<", ""):
        text = text.replace(char, _UNICODE_ESCAPES[char])
    return text


def should_compress(raw_size: int, config: Config) -> bool:
    """Decide whether a payload of raw_size bytes gets compressed.

    Args:
        raw_size: Size of the serialized JSON in UTF-8 bytes.
        config: Application configuration.

    Returns:
        True when compression is enabled and the payload reaches the threshold.
    """
    return bool(config.PAYLOAD_COMPRESSION_ENABLED) and raw_size >= max(0, int(config.PAYLOAD_COMPRESSION_MIN_BYTES))


def compress_text(text: str, config: Config) -> str:
    """Gzip and base64-encode text deterministically (mtime fixed at zero).

    Args:
        text: Text to compress.
        config: Application configuration (PAYLOAD_COMPRESSION_LEVEL).

    Returns:
        ASCII base64 string of the gzip stream.
    """
    level = min(9, max(1, int(config.PAYLOAD_COMPRESSION_LEVEL)))
    packed = gzip.compress(text.encode("utf-8"), compresslevel=level, mtime=0)
    return base64.b64encode(packed).decode("ascii")


def payload_script(
    element_id: str, payload: object, config: Config, compact: bool = True, escape: str = "<>&",
) -> str:
    """Render the script element carrying a page payload.

    Plain payloads keep the exact serialization each page used before
    (separators and escaped characters), so small pages are unchanged.

    Args:
        element_id: DOM id the page loader reads.
        payload: JSON-serializable payload.
        config: Application configuration.
        compact: True for "," / ":" separators, False for json.dumps defaults.
        escape: Characters unicode-escaped in plain JSON ("<" always is).

    Returns:
        A plain application/json script element, or a gzip+base64
        application/octet-stream element when the payload is large.
    """
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":") if compact else None)
    safe_id = html.escape(element_id, quote=True)
    if should_compress(len(data.encode("utf-8")), config):
        return (f'<script type="application/octet-stream" id="{safe_id}" '
                f'data-encoding="{PAYLOAD_ENCODING_GZIP}">{compress_text(data, config)}</script>')
    return f'<script type="application/json" id="{safe_id}">{escape_json_for_script(data, escape)}</script>'


def read_payload_script(document: str, element_id: str) -> Optional[object]:
    """Decode a payload script element from a rendered page (plain or gzip+base64).

    Args:
        document: Rendered HTML document.
        element_id: DOM id of the payload script element.

    Returns:
        The decoded JSON value, or None when the element is missing or empty.
    """
    pattern = re.compile(
        r'<script type="application/(?:json|octet-stream)" id="' + re.escape(element_id)
        + r'"(?P<attrs>[^>]*)>(?P<body>.*?)</script>', re.S,
    )
    match = pattern.search(document)
    if match is None or not match.group("body").strip():
        return None
    body = match.group("body")
    if PAYLOAD_ENCODING_GZIP in match.group("attrs"):
        body = gzip.decompress(base64.b64decode(body)).decode("utf-8")
    return json.loads(body)
