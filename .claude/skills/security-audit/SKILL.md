
---
name: Security Audit
description: Scans code for vulnerabilities, injection risks, and insecure patterns
---

# Security Audit

## Purpose

Identify security vulnerabilities in application code before they reach production.

## Instructions

Scan the codebase for:

1. **Injection Attacks** — SQL injection, command injection, XSS, template injection
2. **Authentication Flaws** — Weak password handling, missing MFA, session fixation
3. **Authorization Gaps** — Missing access controls, privilege escalation paths
4. **Data Exposure** — Hardcoded secrets, verbose error messages, unencrypted PII
5. **Dependency Risks** — Known CVEs in third-party packages

## Severity Classification

- **Critical** — Exploitable in production with high impact
- **High** — Exploitable but requires specific conditions
- **Medium** — Defense-in-depth concern
- **Low** — Informational finding or best practice deviation
