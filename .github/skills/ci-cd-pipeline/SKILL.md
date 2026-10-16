
---
name: CI/CD Pipeline Builder
description: Creates and optimizes GitHub Actions CI/CD workflows
---

# CI/CD Pipeline Builder

## Purpose

Design and maintain CI/CD pipelines using GitHub Actions that are fast, reliable, and secure.

## Instructions

When building pipelines:

1. **Build Stage** — Configure dependency caching, parallel jobs, and matrix builds for multi-version testing
2. **Test Stage** — Run unit, integration, and E2E tests with proper service containers (Postgres, Redis)
3. **Security Stage** — Include SAST scanning, dependency audit, and secret detection steps
4. **Deploy Stage** — Implement blue-green or canary deployments with automatic rollback
5. **Notifications** — Send Slack/email alerts on failure with actionable error summaries

## Best Practices

- Pin action versions to full SHA for supply-chain security
- Use `concurrency` groups to cancel redundant runs
- Store secrets in GitHub Secrets, never in workflow files
- Keep total pipeline duration under 10 minutes
