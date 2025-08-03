from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # view logic for creating a book
    # Example: show a form or process POST data
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # view logic for editing a book
    # Example: show a form or process POST data
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # view logic for deleting a book
    # Example: delete the book instance
    pass

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    # view logic for viewing a single book
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # view logic for listing all books
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})