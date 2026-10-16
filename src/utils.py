
"""Shared utilities for logging configuration and config loading."""

import json
import logging
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def configure_logging(level: str = "INFO") -> None:
    """Set up structured JSON logging to stdout."""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            '{"timestamp":"%(asctime)s","level":"%(levelname)s","logger":"%(name)s","message":"%(message)s"}'
        )
    )
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO), handlers=[handler])
    logger.debug("Logging configured at %s level", level)


def load_config(config_path: str | None = None) -> dict[str, Any]:
    """Load application configuration from claude.json at the project root.

    Args:
        config_path: Optional override path. Falls back to PROJECT_ROOT/claude.json.

    Returns:
        Parsed configuration dictionary.
    """
    path = Path(config_path) if config_path else PROJECT_ROOT / "claude.json"
    if not path.exists():
        logger.warning("Config file not found at %s, using defaults", path)
        return {"model": "default", "context_window": 100000}

    with open(path, encoding="utf-8") as fh:
        config: dict[str, Any] = json.load(fh)

    logger.info("Loaded config from %s", path)
    return config
