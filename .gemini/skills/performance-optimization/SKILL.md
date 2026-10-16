
---
name: Performance Optimization
description: Identifies performance bottlenecks and suggests optimizations
---

# Performance Optimization

## Purpose

Detect and resolve performance bottlenecks in application code, database queries, and infrastructure configuration.

## Instructions

When optimizing performance:

1. **Database Queries** — Identify N+1 queries, missing indexes, and unnecessary joins; suggest query rewrites
2. **Caching Strategy** — Recommend caching layers (in-memory, Redis, CDN) based on access patterns
3. **Async Operations** — Convert blocking I/O to async where the runtime supports it
4. **Memory Management** — Find memory leaks, excessive allocations, and opportunities for object pooling
5. **Algorithm Complexity** — Flag O(n^2) or worse algorithms and suggest more efficient alternatives

## Benchmarking

- Profile before and after changes using `cProfile` or `py-spy`
- Measure p50, p95, and p99 latencies
- Set performance budgets for critical paths (e.g., API response < 200ms)
