# Authentication and Permissions in Django REST Framework

## Overview

This API uses Django REST Framework's token authentication to secure all endpoints. Only authenticated users can access or modify data.

## Setup

1. Add `rest_framework` and `rest_framework.authtoken` to `INSTALLED_APPS` in `settings.py`.
2. Set up authentication and permissions in the `REST_FRAMEWORK` settings block.
3. Run `python manage.py migrate` to create tables for token management.

## How It Works

- All API endpoints require authentication (see `IsAuthenticated` permission in each view).
- Obtain an authentication token by sending a POST request to `/api/auth-token/` with username and password.
- Use this token in the `Authorization: Token <your-token>` header for all requests.

## Example: Obtain Token

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"youruser", "password":"yourpass"}' \
     http://127.0.0.1:8000/api/auth-token/
```

## Example: Authenticated Request

```bash
curl -H "Authorization: Token <your-token>" \
     http://127.0.0.1:8000/api/books_all/
```

## Permissions

- Only authenticated users can access and modify API data.
- Permissions are set in each view using `permission_classes = [IsAuthenticated]`.

## Custom Permissions

You can add custom permissions by creating new classes in `api/permissions.py` and referencing them in your viewsets.