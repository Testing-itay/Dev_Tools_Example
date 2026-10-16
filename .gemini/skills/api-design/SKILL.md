
---
name: API Design Reviewer
description: Reviews API designs for RESTful best practices and consistency
---

# API Design Reviewer

## Purpose

Ensure API endpoints follow RESTful conventions, maintain consistency, and provide a good developer experience.

## Instructions

When reviewing API designs:

1. **Resource Naming** — Use plural nouns, kebab-case, and consistent hierarchy (e.g., `/users/{id}/orders`)
2. **HTTP Methods** — Verify correct use of GET, POST, PUT, PATCH, DELETE semantics
3. **Status Codes** — Ensure appropriate codes (201 Created, 204 No Content, 404 Not Found, 422 Unprocessable)
4. **Pagination** — Require cursor-based or offset pagination for collection endpoints
5. **Versioning** — Use URL path versioning (`/v1/`) or Accept header versioning

## Validation Checklist

- Request/response schemas documented with examples
- Error responses follow RFC 7807 (Problem Details)
- Rate limiting headers included (X-RateLimit-Limit, X-RateLimit-Remaining)
- CORS configuration appropriate for intended consumers
- Authentication requirements clearly specified per endpoint
