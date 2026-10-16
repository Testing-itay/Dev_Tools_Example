
---
name: Monitoring Setup
description: Configures application monitoring, alerting, and observability
---

# Monitoring Setup

## Purpose

Establish comprehensive observability across applications with metrics, logs, and traces.

## Instructions

When setting up monitoring:

1. **Metrics** — Instrument key business and infrastructure metrics using Prometheus/OpenTelemetry (request rate, error rate, latency, saturation)
2. **Logging** — Configure structured JSON logging with correlation IDs, severity levels, and contextual fields
3. **Tracing** — Implement distributed tracing with OpenTelemetry SDK for cross-service request tracking
4. **Alerting** — Define alert rules based on SLO burn rates with appropriate escalation policies
5. **Dashboards** — Create Grafana dashboards with RED (Rate, Errors, Duration) and USE (Utilization, Saturation, Errors) views

## Alert Severity Levels

| Level    | Response Time | Example                          |
|----------|--------------|----------------------------------|
| Critical | 5 minutes    | Service down, data loss risk     |
| Warning  | 30 minutes   | Error rate above SLO threshold   |
| Info     | Next sprint  | Disk usage trending upward       |
