# `readmenator._layers`

> Source: [readmenator/_layers.py:1](../../readmenator/_layers.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Architectural layer detection for the readmenator knowledge graph.

Infers architectural layers (presentation, business logic, data access,
infrastructure, testing, configuration) from file paths, naming
conventions, and import patterns. No external API calls.

## Contents

- **Classes:** [`LayerDetector`](#layerdetector)

## Classes

<a id="layerdetector"></a>

### `LayerDetector`

`class` | [readmenator/_layers.py:17](../../readmenator/_layers.py#L17)

```python
class LayerDetector
```

Detects architectural layers in a codebase.

Assigns each file to a layer based on path patterns, naming
conventions, and imported frameworks. Returns a mapping that
can enrich documentation and analysis. No config dependency.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`detect`](#layerdetector-detect) | method | Assign each file node to an architectural layer. |
| [`layer_summary`](#layerdetector-layer_summary) | staticmethod | Count files per layer. |

<a id="layerdetector-detect"></a>

#### `LayerDetector.detect`

`method` | [readmenator/_layers.py:83](../../readmenator/_layers.py#L83)

```python
def detect(self, nodes: List[Node], edges: List[Edge]) -> Dict[str, str]
```

Assign each file node to an architectural layer.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes. |
| `edges` | `List[Edge]` |  | Import edges. |

**Returns:** `Dict[str, str]` - Dict mapping node_id to layer name.

*Called by:* [`readmenatorApplication.analytics`](readmenator._app.py.md#readmenatorapplication-analytics), [`readmenatorApplication.audit_deep`](readmenator._app.py.md#readmenatorapplication-audit_deep), [`readmenatorApplication.build_graphrag`](readmenator._app.py.md#readmenatorapplication-build_graphrag), [`readmenatorApplication.detect_layers`](readmenator._app.py.md#readmenatorapplication-detect_layers), [`readmenatorApplication.explorer_state`](readmenator._app.py.md#readmenatorapplication-explorer_state), [`readmenatorApplication.export_bundlegraph`](readmenator._app.py.md#readmenatorapplication-export_bundlegraph), [`readmenatorApplication.export_diagram`](readmenator._app.py.md#readmenatorapplication-export_diagram), [`readmenatorApplication.export_diagrams`](readmenator._app.py.md#readmenatorapplication-export_diagrams), [`readmenatorApplication.export_forcegraph`](readmenator._app.py.md#readmenatorapplication-export_forcegraph), [`readmenatorApplication.export_pages`](readmenator._app.py.md#readmenatorapplication-export_pages), [`readmenatorApplication.export_video`](readmenator._app.py.md#readmenatorapplication-export_video), [`readmenatorApplication.export_wiki`](readmenator._app.py.md#readmenatorapplication-export_wiki) and 7 more

<a id="layerdetector-layer_summary"></a>

#### `LayerDetector.layer_summary`

`staticmethod` | [readmenator/_layers.py:189](../../readmenator/_layers.py#L189)

Decorators: `@staticmethod`

```python
def layer_summary(layers: Dict[str, str]) -> Dict[str, int]
```

Count files per layer.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `layers` | `Dict[str, str]` |  | Mapping from detect(). |

**Returns:** `Dict[str, int]` - Dict of layer_name -> file_count.

*Called by:* [`readmenatorApplication.detect_layers`](readmenator._app.py.md#readmenatorapplication-detect_layers), [`readmenatorApplication.run`](readmenator._app.py.md#readmenatorapplication-run)

---
