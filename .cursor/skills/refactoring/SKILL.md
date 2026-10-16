
---
name: Refactoring Assistant
description: Identifies and applies code refactoring patterns to improve maintainability
---

# Refactoring Assistant

## Purpose

Improve code quality by identifying and applying well-known refactoring patterns while preserving behavior.

## Instructions

When refactoring code:

1. **Extract Method** — Break long functions into smaller, named pieces
2. **Replace Conditional with Polymorphism** — Convert complex if/elif chains to class hierarchies
3. **Introduce Parameter Object** — Group related parameters into data classes
4. **Remove Dead Code** — Eliminate unreachable or unused code paths
5. **Simplify Boolean Expressions** — Apply De Morgan's laws and short-circuit evaluation

## Safety Checks

- Ensure all existing tests pass before and after refactoring
- Make atomic commits — one refactoring pattern per commit
- Never change public API signatures without explicit approval
- Document the refactoring pattern applied in the commit message
