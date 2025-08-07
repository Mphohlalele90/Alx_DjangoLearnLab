## API Testing Strategy

- Tests are implemented in `/api/test_views.py` using Django's `APITestCase`.
- Each test covers one aspect of the CRUD operations, filtering, searching, and permissions.
- To run the tests: `python manage.py test api`
- If any test fails, review the error message for details on the failure.

### Test Cases Overview

- Create Book: Tests that a book can be created via POST.
- List Books: Tests that all books are listed via GET.
- Update Book: Tests PUT/PATCH update functionality.
- Delete Book: Tests DELETE removes the book.
- Search/Filter: Tests search and filter parameters.
- Permissions: Tests endpoints with/without authentication.