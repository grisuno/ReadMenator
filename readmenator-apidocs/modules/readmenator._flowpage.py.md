# `readmenator._flowpage`

> Source: [readmenator/_flowpage.py:1](../../readmenator/_flowpage.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Interactive SVG viewer for laid-out architecture and execution-flow diagrams.

The diagrams arrive already placed by readmenator._flowlayout, so the
page only draws: no Mermaid, no CDN, no network. Every diagram gets a
card with its reading guide, a toolbar (fit width, 100 %, zoom in/out,
fullscreen, SVG download), drag to pan, Ctrl/Cmd + wheel to zoom,
hover highlighting of a node's arrows, and a detail panel on click
(signature, docstring summary, called functions with their docs,
component files with purposes and importer counts, a link into the API
reference). Themes follow CSS variables, so the same code serves the
standalone page and the API reference browser.

## Contents

- **Functions:** [`flows_payload_json`](#flows_payload_json), [`render_flows_page`](#render_flows_page), [`flow_thumbnail_svg`](#flow_thumbnail_svg)
- **Constants:** [`FLOW_VIEWER_CSS`](#flow_viewer_css), [`FLOW_VIEWER_JS`](#flow_viewer_js)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_readmenator__flowpage_py__render_flows_page(["render_flows_page"])
    n_readmenator__config_py__Config["_config.Config"]
    n_readmenator__htmlpack_py__payload_script["_htmlpack.payload_script"]
    n_readmenator__flowpage_py__render_flows_page -.-> n_readmenator__config_py__Config
    n_readmenator__flowpage_py__render_flows_page -.-> n_readmenator__htmlpack_py__payload_script
```

## Functions

<a id="flows_payload_json"></a>

### `flows_payload_json`

`function` | [readmenator/_flowpage.py:221](../../readmenator/_flowpage.py#L221)

```python
def flows_payload_json(graphs: List[FlowGraph], api_href: str = '') -> str
```

Serialise laid-out graphs for embedding in a page (angle brackets and ampersands escaped).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `graphs` | `List[FlowGraph]` |  |  |
| `api_href` | `str` | `''` |  |

**Returns:** `str`

---

<a id="render_flows_page"></a>

### `render_flows_page`

`function` | [readmenator/_flowpage.py:227](../../readmenator/_flowpage.py#L227)

```python
def render_flows_page(graphs: List[FlowGraph], project_name: str, api_href: str = '', config: Optional[Config] = None) -> str
```

Render the standalone architecture and execution-flow page.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `graphs` | `List[FlowGraph]` |  | Laid-out graphs from build_flow_graphs(). |
| `project_name` | `str` |  | Display name. |
| `api_href` | `str` | `''` | Relative link to the API reference index.html ("" hides links). |
| `config` | `Optional[Config]` | `None` | Application configuration (payload compression); defaults to Config(). |

**Returns:** `str` - Complete self-contained HTML document (zero external requests).

*Calls:* [`Config`](readmenator._config.py.md#config), [`payload_script`](readmenator._htmlpack.py.md#payload_script)

*Called by:* [`ApiDocsWriter.write`](readmenator._apidocs_render.py.md#apidocswriter-write)

---

<a id="flow_thumbnail_svg"></a>

### `flow_thumbnail_svg`

`function` | [readmenator/_flowpage.py:251](../../readmenator/_flowpage.py#L251)

```python
def flow_thumbnail_svg(graph: FlowGraph, width: int, height: int) -> str
```

Render a small preview of a laid-out diagram for gallery cards.

Only numbers and fixed colors reach the markup (no text), so nothing
needs escaping.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `graph` | `FlowGraph` |  | Laid-out graph (architecture tiers look best). |
| `width` | `int` |  | Thumbnail width in pixels. |
| `height` | `int` |  | Thumbnail height in pixels. |

**Returns:** `str` - ``<svg class="thumb" ...>`` markup, or "" for an empty graph.

---

## Constants

<a id="flow_viewer_css"></a>

### `FLOW_VIEWER_CSS`

`constant` | [readmenator/_flowpage.py:27](../../readmenator/_flowpage.py#L27)

```python
FLOW_VIEWER_CSS
```

---

<a id="flow_viewer_js"></a>

### `FLOW_VIEWER_JS`

`constant` | [readmenator/_flowpage.py:58](../../readmenator/_flowpage.py#L58)

```python
FLOW_VIEWER_JS
```

---
