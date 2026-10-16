
---
name: Dependency Analysis
description: Analyzes project dependencies for vulnerabilities, license issues, and updates
---

# Dependency Analysis

## Purpose

Maintain a healthy dependency tree by identifying vulnerabilities, license conflicts, and outdated packages.

## Instructions

When analyzing dependencies:

1. **Vulnerability Scan** — Cross-reference all packages against CVE databases (NVD, OSV, GitHub Advisory)
2. **License Compliance** — Flag packages with GPL, AGPL, or other copyleft licenses that conflict with project licensing
3. **Update Assessment** — Identify outdated packages and assess breaking change risk for major version bumps
4. **Transitive Dependencies** — Trace indirect dependencies that introduce risk
5. **Supply Chain** — Check for typosquatting, maintainer changes, and low-reputation packages

## Output

Generate a dependency report with:
- Package name and current version
- Latest available version
- Known vulnerabilities (CVE IDs)
- License type
- Recommended action (update, replace, pin, remove)
