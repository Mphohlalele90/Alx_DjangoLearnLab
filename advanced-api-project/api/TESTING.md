# API Testing Strategy

## Overview
This document summarizes the testing approach for the Django REST Framework Book API endpoints.

## Testing Scope
- **CRUD operations**: Create, Read, Update, Delete for Book model.
- **Filtering, Searching, Ordering**: Ensures query params work as expected.
- **Permissions/Authentication**: Verifies unauthorized users cannot write/modify data.

## Test Environment
- Tests use Django's `TestCase` and the Django REST Framework APIClient.
- Tests run against an isolated in-memory test database.
- The production or development database is not affected.

## How to Run Tests

```bash
python manage.py test api
```

## Test Cases

- **Create Book**: Authenticated user can create a book; data is validated and saved.
- **Create Book [fail]**: Unauthenticated user cannot create a book.
- **List Books**: Returns all books.
- **Update Book**: Authenticated user can update a book; changes are saved.
- **Delete Book**: Authenticated user can delete a book; book is removed from DB.
- **Filter/Search/Order**: Query params for filtering (by author), searching (by title), and ordering (by price) work and return correct results.
- **Permissions**: Unauthenticated users cannot update or delete books.

## Interpreting Test Results
- **OK**: All tests pass; endpoints behave as expected.
- **FAIL**: Test output will indicate which test(s) failed and why. Review the error message and traceback for details.

## Notes
- Add more tests for edge cases (e.g., invalid data, missing fields, pagination).
- Update this documentation as the API evolves.
