
# Claude Code — Project Instructions

## Context

This is a Python application demonstrating multi-agent AI tooling. When working in this project:

1. Always check existing tests before modifying business logic
2. Run `pytest` before suggesting any changes are complete
3. Prefer small, focused commits with descriptive messages
4. Security-sensitive code must include input validation

## Architecture

- `src/app.py` — Main application entry point (FastAPI)
- `src/utils.py` — Shared utilities (logging, config)
- `lib/ai-skills/` — Reusable AI skill definitions

## Coding Standards

- Python 3.11+
- Type annotations required
- Docstrings in Google format
- Maximum cyclomatic complexity: 10
