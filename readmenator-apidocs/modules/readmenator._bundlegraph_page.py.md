# `readmenator._bundlegraph_page`

> Source: [readmenator/_bundlegraph_page.py:1](../../readmenator/_bundlegraph_page.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

HTML page template for the edge bundle explorer.

The template is one self-contained document with placeholders
(__TITLE__, __HOME__, __EXPLORER__, __DATA__, __SETTINGS__) filled by
BundleGraphRenderer.render in a single regex pass. Everything is drawn
on one canvas with no external requests: the 2D view lays files on a
circle grouped by community, the 3D view lays them on a sphere of
community caps projected through a small perspective camera, and in
both every import is routed through the community hierarchy as a
B-spline whose bundling strength (beta) is recomputed live in the page.

## Contents

- **Constants:** [`BUNDLEGRAPH_PAGE_TEMPLATE`](#bundlegraph_page_template)

## Constants

<a id="bundlegraph_page_template"></a>

### `BUNDLEGRAPH_PAGE_TEMPLATE`

`constant` | [readmenator/_bundlegraph_page.py:15](../../readmenator/_bundlegraph_page.py#L15)

```python
BUNDLEGRAPH_PAGE_TEMPLATE
```

---
