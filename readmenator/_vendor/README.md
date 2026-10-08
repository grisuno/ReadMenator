# Vendored frontend assets

`force-graph.min.js` — force-graph 2D library (vasturiano), UMD build,
downloaded from `https://cdn.jsdelivr.net/npm/force-graph@1/`
(version 1.52.0 at vendoring time). MIT licensed.

It is copied next to every exported force-graph page
(`readmenator-maps/vendor/force-graph.min.js`) so the explorer works
offline and via `file://` without CDN access. The page falls back to
the CDN copy when the local file is missing. The 3D view still loads
its engine from CDN on demand.
