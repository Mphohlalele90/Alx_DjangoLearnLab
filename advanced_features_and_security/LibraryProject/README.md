# LibraryProject

## Permissions & Groups Setup

This project uses custom permissions and groups to control access for users. The key permissions are defined as:

- `can_create`: Allows user to create new objects (e.g., books, authors).
- `can_edit`: Allows user to edit existing objects.

### How Permissions Work

- Permissions are assigned to groups (e.g., "Editors", "Creators").
- Users are added to groups via the Django admin or programmatically.
- Views and admin classes check for these permissions using Django's `user.has_perm()` method.

### Example Usage

```python
# In bookshelf/models.py
from django.contrib.auth.models import Permission

class Book(models.Model):
    # model fields...

    class Meta:
        permissions = (
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
        )

# In bookshelf/views.py
def edit_book(request, pk):
    if not request.user.has_perm('bookshelf.can_edit'):
        return HttpResponseForbidden("You do not have permission to edit books.")
    # ...rest of view code...

def create_book(request):
    if not request.user.has_perm('bookshelf.can_create'):
        return HttpResponseForbidden("You do not have permission to create books.")
    # ...rest of view code...
```

### Setup Instructions

1. **Apply Migrations**
   ```
   python manage.py migrate
   ```
2. **Assign Permissions to Groups**
   - Go to `/admin`, create groups (e.g., "Editors", "Creators").
   - Assign `can_create`, `can_edit` permissions to the relevant groups.
   - Add users to these groups.

3. **Check Permissions in Views**
   - Use `request.user.has_perm('bookshelf.can_edit')` or `request.user.has_perm('bookshelf.can_create')` to check permissions in your views.

---

For more details, see comments in the relevant model and view files.# LibraryProject Intial set-up
