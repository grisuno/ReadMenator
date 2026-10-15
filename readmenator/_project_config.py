"""Per-project persistent configuration (readmenator.toml).

The generic defaults live in Config (_config.py). Project-specific
choices -- which deliverables are built, under which directory names,
whether the GitHub wiki is published, scan scope, and viewer tuning --
live in a ``readmenator.toml`` file at the analysed project root.

On every ``run``/``rebuild`` the application ensures the file exists
(creating it from an embedded template when missing, never overwriting
an existing file) and then loads it as the source of truth for the
allow-listed keys. Explicit CLI flags always win over the TOML file:
a field whose current value already differs from the Config default is
left untouched by the TOML load.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import fields, replace
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

from readmenator._config import Config

logger = logging.getLogger(__name__)

PROJECT_CONFIG_VERSION = 4

#: Allow-listed TOML keys: (section, key) -> Config field name.
TOML_MAP: Dict[Tuple[str, str], str] = {
    ("project", "name"): "PROJECT_NAME",
    ("branding", "name"): "PROJECT_NAME",
    ("branding", "author"): "PROJECT_AUTHOR",
    ("branding", "description"): "PROJECT_DESCRIPTION",
    ("branding", "github_url"): "PROJECT_GITHUB_URL",
    ("branding", "pages_url"): "PROJECT_PAGES_URL",
    ("branding", "home_url"): "PROJECT_HOME_URL",
    ("branding", "logo_url"): "PROJECT_LOGO_URL",
    ("branding", "accent"): "PROJECT_ACCENT",
    ("branding", "accent2"): "PROJECT_ACCENT2",
    ("outputs", "agent_enabled"): "AGENT_OUTPUT_ENABLED",
    ("outputs", "agent_dir"): "AGENT_OUTPUT_DIR",
    ("outputs", "wiki_enabled"): "WIKI_ENABLED",
    ("outputs", "wiki_dir"): "WIKI_OUTPUT_DIR",
    ("outputs", "apidocs_enabled"): "APIDOCS_ENABLED",
    ("outputs", "apidocs_dir"): "APIDOCS_OUTPUT_DIR",
    ("outputs", "graphrag_enabled"): "GRAPHRAG_ENABLED",
    ("outputs", "graphrag_dir"): "GRAPHRAG_OUTPUT_DIR",
    ("outputs", "maps_dir"): "DIAGRAM_OUTPUT_DIR",
    ("outputs", "pages_dir"): "DIAGRAM_PAGES_DIR",
    ("outputs", "components_enabled"): "COMPONENTS_ENABLED",
    ("outputs", "components_dir"): "COMPONENTS_OUTPUT_DIR",
    ("outputs", "rules_enabled"): "RULE_GEN_ENABLED",
    ("outputs", "rules_dir"): "RULE_GEN_OUTPUT_DIR",
    ("outputs", "forcegraph_enabled"): "FORCEGRAPH_ENABLED",
    ("outputs", "forcegraph_file"): "FORCEGRAPH_OUTPUT",
    ("outputs", "bundle_enabled"): "BUNDLEGRAPH_ENABLED",
    ("outputs", "bundle_file"): "BUNDLEGRAPH_OUTPUT",
    ("outputs", "flows_file"): "FLOWS_OUTPUT",
    ("outputs", "diagrams_enabled"): "DIAGRAM_ENABLED",
    ("outputs", "video_enabled"): "VIDEO_ENABLED",
    ("outputs", "video_file"): "VIDEO_OUTPUT",
    ("outputs", "sarif_enabled"): "SARIF_ENABLED",
    ("features", "security_enabled"): "SECURITY_ENABLED",
    ("features", "privacy_mode"): "PRIVACY_MODE",
    ("features", "gitignore_aware"): "GITIGNORE_AWARE",
    ("features", "gh_wiki_enabled"): "GH_WIKI_ENABLED",
    ("features", "gh_wiki_remote"): "GH_WIKI_REMOTE",
    ("features", "memory_enabled"): "MEMORY_ENABLED",
    ("features", "skills_enabled"): "SKILLS_ENABLED",
    ("features", "concept_enabled"): "CONCEPT_ENABLED",
    ("features", "hotspots_enabled"): "HOTSPOTS_ENABLED",
    ("features", "taint_enabled"): "TAINT_ENABLED",
    ("features", "linter_enabled"): "LINTER_ENABLED",
    ("viewer", "theme"): "DIAGRAM_THEME",
    ("viewer", "preset"): "DIAGRAM_PRESET",
    ("viewer", "motion_enabled"): "DIAGRAM_MOTION_ENABLED",
    ("viewer", "mode"): "FORCEGRAPH_MODE",
    ("viewer", "label_top_n"): "FORCEGRAPH_LABEL_TOP_N",
    ("viewer", "label_zoom"): "FORCEGRAPH_LABEL_ZOOM",
    ("viewer", "charge"): "FORCEGRAPH_CHARGE",
    ("viewer", "link_distance"): "FORCEGRAPH_LINK_DISTANCE",
    ("viewer", "link_strength"): "FORCEGRAPH_LINK_STRENGTH",
    ("viewer", "hulls_enabled"): "FORCEGRAPH_HULLS_ENABLED",
    ("viewer", "particles"): "FORCEGRAPH_PARTICLES_ON_HIGHLIGHT",
    ("viewer", "bundle_beta"): "BUNDLEGRAPH_BETA",
    ("viewer", "html_style"): "HTML_TEMPLATE_STYLE",
    ("messages", "readme_heading"): "MSG_README_HEADING",
    ("messages", "readme_intro"): "MSG_README_INTRO",
    ("messages", "readme_agents_line"): "MSG_README_AGENTS_LINE",
    ("messages", "readme_developers_line"): "MSG_README_DEVELOPERS_LINE",
    ("messages", "readme_regen_command"): "MSG_README_REGEN_COMMAND",
    ("messages", "agent_heading"): "MSG_AGENT_HEADING",
    ("messages", "agent_intro"): "MSG_AGENT_INTRO",
    ("messages", "agent_extra"): "MSG_AGENT_EXTRA",
    ("messages", "folder_notice"): "MSG_FOLDER_NOTICE",
    ("maps", "sourceview_max_files"): "SOURCEVIEW_MAX_FILES",
    ("maps", "sourceview_max_total_chars"): "SOURCEVIEW_MAX_TOTAL_CHARS",
    ("scan", "include_dirs"): "SCAN_INCLUDE_DIRS",
    ("scan", "exclude_patterns"): "SCAN_EXCLUDE_PATTERNS",
    ("scan", "max_file_mb"): "MAX_FILE_SIZE_MB",
    ("scan", "max_depth"): "MAX_DIRECTORY_DEPTH",
}

#: Reverse lookup: Config field -> (section, key).
CONFIG_TO_TOML: Dict[str, Tuple[str, str]] = {v: k for k, v in TOML_MAP.items()}

#: Viewer keys (TOML [viewer] keys) exposed in maps config.json + modal.
VIEWER_TOML_KEYS = (
    "theme", "preset", "motion_enabled", "mode", "label_top_n",
    "label_zoom", "charge", "link_distance", "link_strength",
    "hulls_enabled", "particles", "bundle_beta", "html_style",
)

#: Branding keys (TOML [branding] keys) exposed in config.json + modal.
BRANDING_TOML_KEYS = (
    "name", "author", "description", "github_url", "pages_url",
    "home_url", "logo_url", "accent", "accent2",
)

#: Message keys (TOML [messages] keys) overriding automated injections.
MESSAGES_TOML_KEYS = (
    "readme_heading", "readme_intro", "readme_agents_line",
    "readme_developers_line", "readme_regen_command", "agent_heading",
    "agent_intro", "agent_extra", "folder_notice",
)

#: Maps budget keys (TOML [maps] keys) for the explorers' source viewer.
MAPS_TOML_KEYS = (
    "sourceview_max_files", "sourceview_max_total_chars",
)


def _toml_str(value: str) -> str:
    """Quote a string for TOML output."""
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
        .replace("\r", "\\r")
    )
    return f'"{escaped}"'


def _toml_value(value: Any) -> str:
    """Render a Python value as a TOML literal."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(_toml_str(str(v)) for v in value) + "]"
    return _toml_str(str(value))


def template_text(config: Optional[Config] = None) -> str:
    """Render the example ``readmenator.toml`` content from Config defaults.

    Args:
        config: Base configuration whose values seed the template.

    Returns:
        TOML document as a string.
    """
    cfg = config or Config()
    lines = [
        "# readmenator.toml -- per-project configuration (v%d)." % PROJECT_CONFIG_VERSION,
        "# Created automatically on `readmenator <dir> --rebuild` when missing.",
        "# This file is the source of truth for project-specific choices;",
        "# generic tuning still lives in readmenator/_config.py.",
        "# CLI flags always win over values set here.",
        "",
        "[project]",
        "# Human-readable project name used in page titles. Empty = directory name.",
        f"name = {_toml_value(getattr(cfg, 'PROJECT_NAME', ''))}",
        "",
        "[branding]",
        "# Project identity shown in every HTML page: footer icons link to",
        "# the analysed project's GitHub and published site, the home icon",
        "# points at the deployed readmenator-maps home, and the accent",
        "# colors re-skin all pages (also editable live in the Config modal).",
        "# All URLs must be absolute http(s) links; empty values hide the item.",
        f"author = {_toml_value(getattr(cfg, 'PROJECT_AUTHOR', ''))}",
        f"description = {_toml_value(getattr(cfg, 'PROJECT_DESCRIPTION', ''))}",
        f"github_url = {_toml_value(getattr(cfg, 'PROJECT_GITHUB_URL', ''))}",
        f"pages_url = {_toml_value(getattr(cfg, 'PROJECT_PAGES_URL', ''))}",
        f"home_url = {_toml_value(getattr(cfg, 'PROJECT_HOME_URL', ''))}",
        f"logo_url = {_toml_value(getattr(cfg, 'PROJECT_LOGO_URL', ''))}",
        f"accent = {_toml_value(getattr(cfg, 'PROJECT_ACCENT', '#22d3ee'))}",
        f"accent2 = {_toml_value(getattr(cfg, 'PROJECT_ACCENT2', '#f472b6'))}",
        "",
        "[outputs]",
        "# Which deliverables are built (enabled) and under which directory/file names.",
        f"agent_enabled = {_toml_value(cfg.AGENT_OUTPUT_ENABLED)}",
        f"agent_dir = {_toml_value(cfg.AGENT_OUTPUT_DIR)}",
        f"wiki_enabled = {_toml_value(cfg.WIKI_ENABLED)}",
        f"wiki_dir = {_toml_value(cfg.WIKI_OUTPUT_DIR)}",
        f"apidocs_enabled = {_toml_value(cfg.APIDOCS_ENABLED)}",
        f"apidocs_dir = {_toml_value(cfg.APIDOCS_OUTPUT_DIR)}",
        f"graphrag_enabled = {_toml_value(cfg.GRAPHRAG_ENABLED)}",
        f"graphrag_dir = {_toml_value(cfg.GRAPHRAG_OUTPUT_DIR)}",
        f"maps_dir = {_toml_value(cfg.DIAGRAM_OUTPUT_DIR)}",
        f"pages_dir = {_toml_value(cfg.DIAGRAM_PAGES_DIR)}",
        f"components_enabled = {_toml_value(cfg.COMPONENTS_ENABLED)}",
        f"components_dir = {_toml_value(cfg.COMPONENTS_OUTPUT_DIR)}",
        f"rules_enabled = {_toml_value(cfg.RULE_GEN_ENABLED)}",
        f"rules_dir = {_toml_value(cfg.RULE_GEN_OUTPUT_DIR)}",
        f"forcegraph_enabled = {_toml_value(cfg.FORCEGRAPH_ENABLED)}",
        f"forcegraph_file = {_toml_value(cfg.FORCEGRAPH_OUTPUT)}",
        f"bundle_enabled = {_toml_value(cfg.BUNDLEGRAPH_ENABLED)}",
        f"bundle_file = {_toml_value(cfg.BUNDLEGRAPH_OUTPUT)}",
        f"flows_file = {_toml_value(cfg.FLOWS_OUTPUT)}",
        f"diagrams_enabled = {_toml_value(cfg.DIAGRAM_ENABLED)}",
        f"video_enabled = {_toml_value(cfg.VIDEO_ENABLED)}",
        f"video_file = {_toml_value(cfg.VIDEO_OUTPUT)}",
        f"sarif_enabled = {_toml_value(cfg.SARIF_ENABLED)}",
        "",
        "[features]",
        "# Analysis features + GitHub wiki publishing for this project.",
        f"security_enabled = {_toml_value(cfg.SECURITY_ENABLED)}",
        f"privacy_mode = {_toml_value(cfg.PRIVACY_MODE)}",
        f"gitignore_aware = {_toml_value(cfg.GITIGNORE_AWARE)}",
        f"gh_wiki_enabled = {_toml_value(cfg.GH_WIKI_ENABLED)}",
        f"gh_wiki_remote = {_toml_value(cfg.GH_WIKI_REMOTE)}",
        f"memory_enabled = {_toml_value(cfg.MEMORY_ENABLED)}",
        f"skills_enabled = {_toml_value(cfg.SKILLS_ENABLED)}",
        f"concept_enabled = {_toml_value(cfg.CONCEPT_ENABLED)}",
        f"hotspots_enabled = {_toml_value(cfg.HOTSPOTS_ENABLED)}",
        f"taint_enabled = {_toml_value(cfg.TAINT_ENABLED)}",
        f"linter_enabled = {_toml_value(cfg.LINTER_ENABLED)}",
        "",
        "[viewer]",
        "# Look-and-feel of readmenator-maps/* pages. Editable live via the",
        "# Config button in every map; use Copy TOML there to persist back here.",
        f"theme = {_toml_value(cfg.DIAGRAM_THEME)}",
        f"preset = {_toml_value(cfg.DIAGRAM_PRESET)}",
        f"motion_enabled = {_toml_value(cfg.DIAGRAM_MOTION_ENABLED)}",
        f"mode = {_toml_value(cfg.FORCEGRAPH_MODE)}",
        f"label_top_n = {_toml_value(cfg.FORCEGRAPH_LABEL_TOP_N)}",
        f"label_zoom = {_toml_value(cfg.FORCEGRAPH_LABEL_ZOOM)}",
        f"charge = {_toml_value(cfg.FORCEGRAPH_CHARGE)}",
        f"link_distance = {_toml_value(cfg.FORCEGRAPH_LINK_DISTANCE)}",
        f"link_strength = {_toml_value(cfg.FORCEGRAPH_LINK_STRENGTH)}",
        f"hulls_enabled = {_toml_value(cfg.FORCEGRAPH_HULLS_ENABLED)}",
        f"particles = {_toml_value(cfg.FORCEGRAPH_PARTICLES_ON_HIGHLIGHT)}",
        f"bundle_beta = {_toml_value(cfg.BUNDLEGRAPH_BETA)}",
        f"html_style = {_toml_value(cfg.HTML_TEMPLATE_STYLE)}",
        "",
        "[scan]",
        "# What gets scanned in this project.",
        f"include_dirs = {_toml_value(tuple(cfg.SCAN_INCLUDE_DIRS))}",
        f"exclude_patterns = {_toml_value(tuple(cfg.SCAN_EXCLUDE_PATTERNS))}",
        f"max_file_mb = {_toml_value(cfg.MAX_FILE_SIZE_MB)}",
        f"max_depth = {_toml_value(cfg.MAX_DIRECTORY_DEPTH)}",
        "",
        "[maps]",
        "# Budgets for the readmenator-maps explorers: how many files embed",
        "# their source for the View button (2D/3D graphs) and the total char",
        "# budget across them. Files over budget show a \"cut by SOURCEVIEW",
        "# budgets\" note instead of source. Raise both and rebuild for big repos.",
        f"sourceview_max_files = {_toml_value(cfg.SOURCEVIEW_MAX_FILES)}",
        f"sourceview_max_total_chars = {_toml_value(cfg.SOURCEVIEW_MAX_TOTAL_CHARS)}",
        "",
        "[messages]",
        "# Overrides for the automated texts readmenator injects into projects",
        "# (README section, agent files, folder READMEs). Empty = built-in",
        "# default. Also editable from the Config modal in any map (Copy TOML).",
        "# Multi-line values use \\n escapes.",
        f"readme_heading = {_toml_value(cfg.MSG_README_HEADING)}",
        f"readme_intro = {_toml_value(cfg.MSG_README_INTRO)}",
        f"readme_agents_line = {_toml_value(cfg.MSG_README_AGENTS_LINE)}",
        f"readme_developers_line = {_toml_value(cfg.MSG_README_DEVELOPERS_LINE)}",
        f"readme_regen_command = {_toml_value(cfg.MSG_README_REGEN_COMMAND)}",
        f"agent_heading = {_toml_value(cfg.MSG_AGENT_HEADING)}",
        f"agent_intro = {_toml_value(cfg.MSG_AGENT_INTRO)}",
        f"agent_extra = {_toml_value(cfg.MSG_AGENT_EXTRA)}",
        f"folder_notice = {_toml_value(cfg.MSG_FOLDER_NOTICE)}",
        "",
    ]
    return "\n".join(lines)


def config_path(project_root: Union[str, Path], config: Optional[Config] = None) -> Path:
    """Return the readmenator.toml path for a project root.

    Args:
        project_root: Project directory.
        config: Optional configuration carrying the filename.

    Returns:
        Absolute path of the TOML file.
    """
    name = (config or Config()).PROJECT_CONFIG_FILENAME
    return Path(project_root).resolve() / name


def ensure_project_config(
    project_root: Union[str, Path], config: Optional[Config] = None
) -> Path:
    """Create ``readmenator.toml`` from the template when missing.

    Never overwrites an existing file and refuses symlinked paths.

    Args:
        project_root: Project directory to configure.
        config: Base configuration seeding the template.

    Returns:
        Path of the ensured TOML file.
    """
    cfg = config or Config()
    target = config_path(project_root, cfg)
    try:
        if target.is_symlink():
            logger.warning("Project config is a symlink, refusing to touch: %s", target)
            return target
    except OSError:
        pass
    if target.is_file():
        return target
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(template_text(cfg), encoding="utf-8")
        logger.info("Project config created: %s", target)
    except OSError:
        logger.warning("Project config creation skipped", exc_info=True)
    return target


def _mini_toml_parse(text: str) -> Dict[str, Dict[str, Any]]:
    """Parse the subset of TOML used by readmenator.toml (no dependencies).

    Supports ``[section]`` headers, ``key = value`` pairs, strings,
    booleans, integers, floats, and single-line string arrays. Comments
    (``#``) and blank lines are ignored.

    Args:
        text: TOML document text.

    Returns:
        Nested mapping of section to key/value pairs.
    """
    out: Dict[str, Dict[str, Any]] = {}
    section = ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            out.setdefault(section, {})
            continue
        if "=" not in line or not section:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = _strip_toml_comment(value).strip()
        if not key or not value:
            continue
        out[section][key] = _mini_toml_value(value)
    return out


def _strip_toml_comment(value: str) -> str:
    """Cut a `#` comment while respecting single/double quoted strings.

    Args:
        value: Raw text after the `=` sign.

    Returns:
        Text without the trailing comment.
    """
    in_single = False
    in_double = False
    escaped = False
    for pos, char in enumerate(value):
        if escaped:
            escaped = False
            continue
        if char == "\\" and in_double:
            escaped = True
            continue
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            return value[:pos]
    return value


def _mini_toml_value(value: str) -> Any:
    """Parse one TOML scalar or string array from the mini parser."""
    low = value.lower()
    if low in ("true", "false"):
        return low == "true"
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        items = []
        current = ""
        in_str = False
        quote = ""
        for char in inner:
            if in_str:
                current += char
                if char == quote:
                    in_str = False
            elif char in ("'", '"'):
                in_str = True
                quote = char
                current += char
            elif char == ",":
                items.append(_mini_toml_value(current.strip()))
                current = ""
            else:
                current += char
        if current.strip():
            items.append(_mini_toml_value(current.strip()))
        return items
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        body = value[1:-1]
        if value[0] == '"':
            body = (
                body.replace("\\\\", "\x00")
                .replace('\\"', '"')
                .replace("\\n", "\n")
                .replace("\\t", "\t")
                .replace("\\r", "\r")
                .replace("\\b", "\b")
                .replace("\\f", "\f")
                .replace("\x00", "\\")
            )
        return body
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def parse_toml(text: str) -> Dict[str, Dict[str, Any]]:
    """Parse TOML text with the stdlib when available, else the mini parser.

    Args:
        text: TOML document text.

    Returns:
        Nested mapping of section to key/value pairs.
    """
    try:
        import tomllib as _tomllib

        data = _tomllib.loads(text)
        if isinstance(data, dict):
            return {str(k): (v if isinstance(v, dict) else {}) for k, v in data.items()}
    except ImportError:
        pass
    except ValueError:
        logger.warning("Project config has TOML syntax errors, ignoring it")
        return {}
    try:
        import tomli as _tomli  # type: ignore

        data = _tomli.loads(text)
        if isinstance(data, dict):
            return {str(k): (v if isinstance(v, dict) else {}) for k, v in data.items()}
    except ImportError:
        pass
    except ValueError:
        logger.warning("Project config has TOML syntax errors, ignoring it")
        return {}
    return _mini_toml_parse(text)


def _field_types() -> Dict[str, Any]:
    """Return Config field names mapped to their default value types."""
    types: Dict[str, Any] = {}
    for field in fields(Config):
        types[field.name] = field.default
    return types


def _coerce(field_name: str, value: Any, default: Any) -> Any:
    """Coerce a TOML value to the Config field type.

    Args:
        field_name: Config field name (for tuple/string decisions).
        value: Raw TOML value.
        default: Config default value defining the target type.

    Returns:
        Coerced value, or the default when coercion fails.
    """
    try:
        if isinstance(default, bool):
            if isinstance(value, bool):
                return value
            if isinstance(value, (int, float)):
                return bool(value)
            if isinstance(value, str):
                low = value.strip().lower()
                if low in ("true", "yes", "1", "on"):
                    return True
                if low in ("false", "no", "0", "off"):
                    return False
            return default
        if isinstance(default, int) and not isinstance(default, bool):
            if isinstance(value, bool):
                return default
            return int(value)
        if isinstance(default, float):
            if isinstance(value, bool):
                return default
            return float(value)
        if isinstance(default, str):
            if isinstance(value, (list, tuple)):
                return ", ".join(str(v) for v in value) if value else default
            return str(value)
        if isinstance(default, tuple):
            if isinstance(value, (list, tuple)):
                return tuple(str(v) for v in value)
            if isinstance(value, str):
                text = value.strip()
                if not text:
                    return ()
                if "," in text:
                    return tuple(part.strip() for part in text.split(",") if part.strip())
                return (text,)
            return default
    except (ValueError, TypeError):
        return default
    return default


def load_project_config(
    project_root: Union[str, Path], base: Optional[Config] = None
) -> Config:
    """Load ``readmenator.toml`` over a base Config (CLI flags win).

    Fields whose base value already differs from the Config default are
    treated as explicit CLI overrides and are never clobbered by TOML.

    Args:
        project_root: Project directory holding readmenator.toml.
        base: Base configuration (defaults plus CLI flags).

    Returns:
        Effective configuration with TOML overrides applied.
    """
    cfg = base or Config()
    defaults = Config()
    target = config_path(project_root, cfg)
    try:
        if target.is_symlink() or not target.is_file():
            return cfg
        text = target.read_text(encoding="utf-8")
    except OSError:
        return cfg
    if not text.strip():
        return cfg
    data = parse_toml(text)
    if not data:
        return cfg
    overrides: Dict[str, Any] = {}
    for (section, key), field_name in TOML_MAP.items():
        section_data = data.get(section)
        if not isinstance(section_data, dict) or key not in section_data:
            continue
        try:
            default = getattr(defaults, field_name)
            current = getattr(cfg, field_name)
        except AttributeError:
            continue
        if current != default:
            continue
        overrides[field_name] = _coerce(field_name, section_data[key], default)
    if not overrides:
        return cfg
    try:
        return replace(cfg, **overrides)
    except (ValueError, TypeError):
        logger.warning("Project config values rejected, using base config")
        return cfg


def display_name(config: Config, fallback: str = "") -> str:
    """Return the configured project name, falling back to a default.

    Args:
        config: Effective configuration.
        fallback: Name used when PROJECT_NAME is empty (directory name).

    Returns:
        Stripped project name or the fallback.
    """
    name = str(getattr(config, "PROJECT_NAME", "") or "").strip()
    return name or fallback


def safe_url(url: Any) -> str:
    """Return a URL only when it is an absolute http(s) link.

    Args:
        url: Raw configured value.

    Returns:
        The stripped URL, or "" when it is not an absolute http(s) link.
    """
    text = str(url or "").strip()
    if text.startswith("https://") or text.startswith("http://"):
        return text
    return ""


def safe_color(value: Any, fallback: str = "") -> str:
    """Return a hex color only when it matches #rgb/#rrggbb/#rrggbbaa.

    Args:
        value: Raw configured value.
        fallback: Value returned when the input is not a hex color.

    Returns:
        The validated color string or the fallback.
    """
    import re as _re

    text = str(value or "").strip()
    if _re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3}(?:[0-9a-fA-F]{2})?)?", text):
        return text
    return fallback


def branding_css(config: Config) -> str:
    """Return a CSS override block with the configured accent colors.

    Args:
        config: Effective configuration.

    Returns:
        CSS text setting --accent/--accent2, or "" when unset/invalid.
    """
    rules = []
    accent = safe_color(getattr(config, "PROJECT_ACCENT", ""), "")
    accent2 = safe_color(getattr(config, "PROJECT_ACCENT2", ""), "")
    if accent:
        rules.append(f"--accent:{accent}")
    if accent2:
        rules.append(f"--accent2:{accent2}")
    if not rules:
        return ""
    return ":root{" + ";".join(rules) + "}"


def viewer_config_dict(config: Config, project_root: Union[str, Path, None] = None) -> Dict[str, Any]:
    """Return the viewer-facing subset of Config for maps pages + config.json.

    Includes the [viewer] keys plus the [branding] identity used by page
    headers, footers, and the Config modal, the [messages] injection
    overrides, and the [maps] source-viewer budgets.

    Args:
        config: Effective configuration.
        project_root: Optional project root used for the meta block.

    Returns:
        JSON-serializable viewer configuration with a _meta block.
    """
    viewer: Dict[str, Any] = {}
    for toml_key in VIEWER_TOML_KEYS:
        field_name = TOML_MAP[("viewer", toml_key)]
        value = getattr(config, field_name, None)
        if isinstance(value, tuple):
            value = list(value)
        viewer[toml_key] = value
    branding: Dict[str, Any] = {}
    for toml_key in BRANDING_TOML_KEYS:
        field_name = TOML_MAP[("branding", toml_key)]
        value = getattr(config, field_name, None)
        if isinstance(value, tuple):
            value = list(value)
        branding[toml_key] = value
    viewer["branding"] = branding
    messages: Dict[str, Any] = {}
    for toml_key in MESSAGES_TOML_KEYS:
        field_name = TOML_MAP[("messages", toml_key)]
        value = getattr(config, field_name, None)
        if isinstance(value, tuple):
            value = list(value)
        messages[toml_key] = value
    viewer["messages"] = messages
    maps: Dict[str, Any] = {}
    for toml_key in MAPS_TOML_KEYS:
        field_name = TOML_MAP[("maps", toml_key)]
        value = getattr(config, field_name, None)
        if isinstance(value, tuple):
            value = list(value)
        maps[toml_key] = value
    viewer["maps"] = maps
    viewer["_meta"] = {
        "version": PROJECT_CONFIG_VERSION,
        "source": config.PROJECT_CONFIG_FILENAME,
        "project": display_name(config, str(Path(project_root).resolve().name) if project_root else ""),
        "generated_at": int(time.time()),
    }
    return viewer


def write_viewer_config(
    maps_dir: Union[str, Path], config: Config,
    project_root: Union[str, Path, None] = None,
) -> Optional[Path]:
    """Write ``config.json`` beside the maps gallery (never fatal).

    Args:
        maps_dir: Directory holding the gallery index.
        config: Effective configuration.
        project_root: Optional project root for the meta block.

    Returns:
        Written file path, or None when the write fails.
    """
    try:
        dest = Path(maps_dir)
        dest.mkdir(parents=True, exist_ok=True)
        target = dest / config.VIEWER_CONFIG_FILENAME
        if target.is_symlink():
            return None
        target.write_text(
            json.dumps(viewer_config_dict(config, project_root), indent=1, sort_keys=True),
            encoding="utf-8",
        )
        return target
    except OSError:
        logger.debug("Viewer config write skipped", exc_info=True)
        return None
