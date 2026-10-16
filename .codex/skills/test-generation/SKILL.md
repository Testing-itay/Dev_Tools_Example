
---
name: Test Generation
description: Generates comprehensive unit and integration tests for existing code
---

# Test Generation

## Purpose

Automatically generate meaningful tests that verify business logic, edge cases, and error handling.

## Instructions

When generating tests:

1. **Unit Tests** — Test individual functions in isolation with mocked dependencies
2. **Integration Tests** — Verify component interactions with real or in-memory backends
3. **Edge Cases** — Cover boundary values, empty inputs, None/null, Unicode, and overflow
4. **Error Paths** — Test exception handling, timeout behavior, and retry logic
5. **Parameterized Tests** — Use `@pytest.mark.parametrize` for data-driven testing

## Conventions

- Use `pytest` as the test framework
- Name test files as `test_<module>.py`
- Use descriptive test names: `test_<function>_<scenario>_<expected_result>`
- Prefer `factory_boy` or fixtures for test data setup
- Target minimum 80% branch coverage
