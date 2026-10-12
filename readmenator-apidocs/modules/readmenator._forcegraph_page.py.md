# `readmenator._forcegraph_page`

> Source: [readmenator/_forcegraph_page.py:1](../../readmenator/_forcegraph_page.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

HTML page template for the force-graph explorer.

The template is a single self-contained document with placeholders
(__TITLE__, __HOME__, __VENDOR_SRC__, __CDN_2D__, __CDN_3D__, __DATA__,
__ANALYTICS__, __SETTINGS__, __LOADER__) filled by ForceGraphRenderer.render.
The graph and analytics payloads are payload script elements (plain JSON,
or gzip+base64 when large) decoded by the shared loader before boot. All
pointer interaction (hover, click, drag, context menu) is hit-tested in
the page against live node positions, so selection never drifts from
what is drawn. The 3D view keeps the WebGL engine for links and physics
and paints flat node glyphs, labels, and group halos on a 2D overlay
projected from the same camera in the same frame.

## Contents

- **Constants:** [`FORCEGRAPH_PAGE_TEMPLATE`](#forcegraph_page_template)

## Constants

<a id="forcegraph_page_template"></a>

### `FORCEGRAPH_PAGE_TEMPLATE`

`constant` | [readmenator/_forcegraph_page.py:17](../../readmenator/_forcegraph_page.py#L17)

```python
FORCEGRAPH_PAGE_TEMPLATE
```

---
