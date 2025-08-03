from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # view logic for creating a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # view logic for editing a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # view logic for deleting a book
    pass

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    # view logic for viewing a book
    pass