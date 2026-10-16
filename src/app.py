
"""AI Agents Demo — Main application entry point."""

import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils import configure_logging, load_config

logger = logging.getLogger(__name__)


class HealthResponse(BaseModel):
    status: str
    version: str


class AgentInfo(BaseModel):
    name: str
    provider: str
    enabled: bool = True


AGENTS: list[AgentInfo] = [
    AgentInfo(name="Claude Code", provider="Anthropic"),
    AgentInfo(name="Codex", provider="OpenAI"),
    AgentInfo(name="Cursor AI", provider="Anysphere"),
    AgentInfo(name="Gemini", provider="Google"),
    AgentInfo(name="GitHub Copilot", provider="GitHub"),
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    config = load_config()
    logger.info("Starting AI Agents Demo", extra={"config": config})
    yield
    logger.info("Shutting down AI Agents Demo")


app = FastAPI(
    title="AI Agents Demo",
    description="Demo API showcasing multi-agent AI development tooling",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return application health status."""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/agents", response_model=list[AgentInfo])
async def list_agents() -> list[AgentInfo]:
    """Return all configured AI agents."""
    return AGENTS


@app.get("/agents/{agent_name}", response_model=AgentInfo)
async def get_agent(agent_name: str) -> AgentInfo:
    """Return a specific AI agent by name."""
    for agent in AGENTS:
        if agent.name.lower() == agent_name.lower():
            return agent
    raise HTTPException(status_code=404, detail=f"Agent '{agent_name}' not found")


@app.get("/stats")
async def get_stats() -> dict[str, Any]:
    """Return aggregated statistics about configured agents and plugins."""
    return {
        "total_agents": len(AGENTS),
        "providers": list({a.provider for a in AGENTS}),
        "enabled_count": sum(1 for a in AGENTS if a.enabled),
    }
