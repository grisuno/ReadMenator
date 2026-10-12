# `readmenator.parsers`

> Source: [readmenator/parsers/__init__.py:1](../../readmenator/parsers/__init__.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Parser factory: maps file extensions to per-language LanguageParser classes.

## Contents

- **Functions:** [`create_parser`](#create_parser)
- **Constants:** [`SUPPORTED_EXTENSIONS`](#supported_extensions)

## Functions

<a id="create_parser"></a>

### `create_parser`

`function` | [readmenator/parsers/__init__.py:70](../../readmenator/parsers/__init__.py#L70)

```python
def create_parser(extension: str, filename: str, config: Config) -> Optional[LanguageParser]
```

Factory: return a parser instance for the given file extension.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `extension` | `str` |  |  |
| `filename` | `str` |  |  |
| `config` | `Config` |  |  |

**Returns:** `Optional[LanguageParser]`

---

## Constants

<a id="supported_extensions"></a>

### `SUPPORTED_EXTENSIONS`

`constant` | [readmenator/parsers/__init__.py:31](../../readmenator/parsers/__init__.py#L31)

```python
SUPPORTED_EXTENSIONS = []
```

---
