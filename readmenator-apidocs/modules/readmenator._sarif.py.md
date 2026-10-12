# `readmenator._sarif`

> Source: [readmenator/_sarif.py:1](../../readmenator/_sarif.py#L1) | language `py` | coverage 75.0% | [API index](../index.md)

SARIF v2.1.0 exporter for security findings (GitHub Code Scanning compatible).

## Contents

- **Classes:** [`SarifExporter`](#sarifexporter)

## Classes

<a id="sarifexporter"></a>

### `SarifExporter`

`class` | [readmenator/_sarif.py:11](../../readmenator/_sarif.py#L11)

```python
class SarifExporter
```

Exports security findings to the SARIF standard format.

SARIF is an OASIS standard format for static analysis tool output.
This exporter produces SARIF v2.1.0 JSON compatible with GitHub
Code Scanning, VS Code SARIF viewer, and other SARIF consumers.

**Attributes**

| Name | Type | Default | Description |
|---|---|---|---|
| [`SARIF_VERSION`](#sarifexporter-sarif_version) |  | `'2.1.0'` |  |
| [`SARIF_SCHEMA`](#sarifexporter-sarif_schema) |  | `'https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json'` |  |
| [`SEVERITY_LEVEL_MAP`](#sarifexporter-severity_level_map) | `Dict[str, str]` | `{'critical': 'error', 'high': 'error', 'medium': 'warning', 'low': 'note', 'info': 'note'}` |  |

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#sarifexporter-__init__) | constructor |  |
| [`export`](#sarifexporter-export) | method | Generate a SARIF v2.1.0 JSON string from security findings. |

<a id="sarifexporter-__init__"></a>

#### `SarifExporter.__init__`

`constructor` | [readmenator/_sarif.py:30](../../readmenator/_sarif.py#L30)

```python
def __init__(self, privacy_mode: bool = False) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `privacy_mode` | `bool` | `False` |  |

*Called by:* [`AnalyzerFactory.sarif`](readmenator._pipeline.py.md#analyzerfactory-sarif)

<a id="sarifexporter-export"></a>

#### `SarifExporter.export`

`method` | [readmenator/_sarif.py:33](../../readmenator/_sarif.py#L33)

```python
def export(self, findings: List[SecurityFinding], project_name: str = 'readmenator') -> str
```

Generate a SARIF v2.1.0 JSON string from security findings.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `findings` | `List[SecurityFinding]` |  | List of SecurityFinding instances. |
| `project_name` | `str` | `'readmenator'` | Name of the scanned project for metadata. |

**Returns:** `str` - SARIF JSON string.

---
