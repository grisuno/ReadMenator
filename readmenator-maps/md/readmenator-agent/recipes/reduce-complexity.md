# Recipe: Reduce File Complexity

Target hotspot: `readmenator/_vendor/force-graph.min.js`
(complexity 0.4, centrality 1.0)

1. Read dependents: `grep -n 'readmenator/_vendor/force-graph.min.js' readmenator-agent/ARCHITECTURE*.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
