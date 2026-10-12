# Subsystem: readmenator (page 5 of 5)
Previous: [KB_readmenator_p4.md](KB_readmenator_p4.md)

## readmenator/_yaralite.py
- Doc: Zero-dependency YARA-lite rule parser and runner.
- Layer: utility
- Language: py
- Symbols:
  - `YaraLiteString` (class, line 24) `class YaraLiteString`
  - `YaraLiteRule` (class, line 33) `class YaraLiteRule`
  - `YaraLiteHit` (class, line 56) `class YaraLiteHit`
  - `YaraLiteMatch` (class, line 66) `class YaraLiteMatch`
  - `parse_yaralite_rules` (function, line 76) `def parse_yaralite_rules(rules_text)`
  - `run_yaralite_rules` (function, line 112) `def run_yaralite_rules(text, rules)`
  - `validate_yaralite_rules` (function, line 139) `def validate_yaralite_rules(rules_text)`
  - `_rule_blocks` (function, line 161) `def _rule_blocks(rules_text)`
  - `_section` (function, line 182) `def _section(body, start_marker, end_marker)`
  - `_parse_meta` (function, line 196) `def _parse_meta(meta_body)`
  - `_parse_strings` (function, line 215) `def _parse_strings(strings_body)`
  - `_strip_comments` (function, line 233) `def _strip_comments(text)`
  - `_decode_yara_string` (function, line 238) `def _decode_yara_string(value)`
  - `_string_hits` (function, line 243) `def _string_hits(text, rule)`
  - `_condition_matches` (function, line 265) `def _condition_matches(condition, hits)`
  - `_confidence` (function, line 305) `def _confidence(value)`
  - `_excerpt` (function, line 322) `def _excerpt(text, offset, length)`
  - `tier` (method, line 42) `def tier(self)`
  - `replace_group` (function, line 270) `def replace_group(match)`
  - `replace_identifier` (function, line 292) `def replace_identifier(match)`
- Imported by: `readmenator/_app.py`, `tests/test_interactive_graph.py`

