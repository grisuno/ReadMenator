# `readmenator._analytics`

> Source: [readmenator/_analytics.py:1](../../readmenator/_analytics.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Corpus analytics aggregations for the readmenator knowledge graph.

Computes the explorer dashboard payloads (attribution funnel,
distributions, scatter, rule yield) from file-level code graphs so the
force-graph explorer and gallery can render an analytics dashboard
from a single payload.

## Contents

- **Classes:** [`AnalyticsBuilder`](#analyticsbuilder)

## Classes

<a id="analyticsbuilder"></a>

### `AnalyticsBuilder`

`class` | [readmenator/_analytics.py:25](../../readmenator/_analytics.py#L25)

```python
class AnalyticsBuilder
```

Builds analytics payloads from scanned topology and findings.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#analyticsbuilder-__init__) | constructor | Initialise with application configuration. |
| [`build`](#analyticsbuilder-build) | method | Build the full analytics payload. |

<a id="analyticsbuilder-__init__"></a>

#### `AnalyticsBuilder.__init__`

`constructor` | [readmenator/_analytics.py:28](../../readmenator/_analytics.py#L28)

```python
def __init__(self, config: Config) -> None
```

Initialise with application configuration.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  | Settings guarding the analytics flag. |

*Called by:* [`ExplorerState.__init__`](readmenator._explorer.py.md#explorerstate-__init__), [`GraphExporter.to_forcegraph`](readmenator._exporter.py.md#graphexporter-to_forcegraph), [`AnalyzerFactory.analytics`](readmenator._pipeline.py.md#analyzerfactory-analytics)

<a id="analyticsbuilder-build"></a>

#### `AnalyticsBuilder.build`

`method` | [readmenator/_analytics.py:36](../../readmenator/_analytics.py#L36)

```python
def build(self, nodes: List[Node], edges: List[Edge], resolved_edges: Optional[List[Edge]] = None, analysis: Optional[AnalysisResult] = None, findings: Optional[List[SecurityFinding]] = None, layers: Optional[Dict[str, str]] = None, v2: Optional[AnalysisResultV2] = None, hotspots: Optional[List[HotspotResult]] = None) -> Dict[str, Any]
```

Build the full analytics payload.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `nodes` | `List[Node]` |  | Scanned file nodes. |
| `edges` | `List[Edge]` |  | Import edges. |
| `resolved_edges` | `Optional[List[Edge]]` | `None` | Optional resolved-import edges. |
| `analysis` | `Optional[AnalysisResult]` | `None` | Optional community and god-node analysis. |
| `findings` | `Optional[List[SecurityFinding]]` | `None` | Optional security findings. |
| `layers` | `Optional[Dict[str, str]]` | `None` | Optional file-to-layer mapping. |
| `v2` | `Optional[AnalysisResultV2]` | `None` | Optional deep analysis results. |
| `hotspots` | `Optional[List[HotspotResult]]` | `None` | Optional hotspot ranking override. |

**Returns:** `Dict[str, Any]` - Analytics dictionary with funnel, distributions, and scatter.

*Called by:* [`ExplorerState.__init__`](readmenator._explorer.py.md#explorerstate-__init__), [`GraphExporter.to_forcegraph`](readmenator._exporter.py.md#graphexporter-to_forcegraph)

---
