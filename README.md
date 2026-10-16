
# AI Agents Demo

A Python application showcasing multi-agent AI development tooling — configured with **Claude Code**, **Codex**, **Cursor AI**, **Gemini**, and **GitHub Copilot**.

## Overview

This repository demonstrates how modern AI coding assistants can be configured side-by-side in a single project. It includes:

- **5 AI Agents** — Claude Code (Anthropic), Codex (OpenAI), Cursor AI (Anysphere), Gemini (Google), GitHub Copilot (GitHub)
- **28 Agent Plugins** — across JSON, TOML, and YAML formats with both enabled and disabled extensions
- **10 MCP Servers** — Model Context Protocol servers in JSON and TOML (with deduplication)
- **12 Agent Skills** — specialized capabilities distributed across 6 skill directories

## Project Structure

```
├── .claude/          # Claude Code agent config, plugins & skills
├── .codex/           # Codex agent config (TOML) & skills
├── .cursor/          # Cursor AI extensions, MCP servers & skills
├── .gemini/          # Gemini extensions (YAML/YML) & skills
├── .github/          # GitHub Copilot config & skills
├── .vscode/          # VS Code extension recommendations
├── lib/ai-skills/    # Shared AI skills (custom prefix path)
├── src/              # Sample Python application
├── mcp-servers.toml  # Root-level MCP server definitions (TOML)
├── claude.json       # Claude Code root config
├── .cursorrules      # Cursor AI project conventions
└── .aiexclude        # Codex AI exclusion patterns
```

## Getting Started

```bash
pip install -r requirements.txt
python src/app.py
```

## Configuration Formats

| Format | Files | Agent |
|--------|-------|-------|
| JSON   | `plugins.json`, `extentions.json`, `extensions.json`, `mcp.json` | Claude, Cursor, VS Code |
| TOML   | `config.toml`, `mcp-servers.toml` | Codex, Root MCP |
| YAML   | `extention.yaml`, `extention.yml`, `copilot.yml` | Gemini, GitHub Copilot |

## License

MIT
