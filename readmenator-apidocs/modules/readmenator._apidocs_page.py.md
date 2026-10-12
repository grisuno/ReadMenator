# `readmenator._apidocs_page`

> Source: [readmenator/_apidocs_page.py:1](../../readmenator/_apidocs_page.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Self-contained HTML browser for the deterministic API reference.

One file, zero external requests: the reference is embedded as JSON
(angle brackets escaped) and rendered client-side with a module tree,
instant search over names, qualnames and summaries, module pages with
signatures, parameter tables, returns, raises, examples, admonitions,
inheritance and call links, a class hierarchy, a general index, a
coverage report, hash deep links, and a dark / light theme that shares
the readmenator theme key.

## Contents

- **Functions:** [`render_api_site`](#render_api_site)

## Functions

<a id="render_api_site"></a>

### `render_api_site`

`function` | [readmenator/_apidocs_page.py:55](../../readmenator/_apidocs_page.py#L55)

```python
def render_api_site(reference: ApiReference, project_name: str, config: Config, architecture_markdown: str = '') -> str
```

Render the standalone HTML API browser.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `reference` | `ApiReference` |  | The API reference. |
| `project_name` | `str` |  | Display name of the project. |
| `config` | `Config` |  | Application configuration. |
| `architecture_markdown` | `str` | `''` | Optional architecture and flow Markdown with Mermaid blocks; rendered as source until the reader asks to load the Mermaid renderer (the only optional network request). |

**Returns:** `str` - Complete HTML document text.

*Called by:* [`ApiDocsWriter.write`](readmenator._apidocs_render.py.md#apidocswriter-write)

---
