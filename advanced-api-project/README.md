# Advanced API Project: Book CRUD API

## API Endpoints

- **GET /api/books/**: List all books (open access)
- **POST /api/books/**: Create a new book (authenticated only)
- **GET /api/books/<id>/**: Retrieve a single book (open access)
- **PUT/PATCH/DELETE /api/books/<id>/**: Update or delete a book (authenticated only)

## Permissions

- Only authenticated users can create, update, or delete books.
- Unauthenticated users can only read/list books.

## Customizations

- Permissions are set per-method in each view using `get_permissions()`.
- All views use Django REST Framework's generic class-based views for DRY, maintainable code.

## Testing

- Use tools like Postman or curl to test CRUD operations and permissions.
- Attempt actions both with and without authentication to verify behavior.