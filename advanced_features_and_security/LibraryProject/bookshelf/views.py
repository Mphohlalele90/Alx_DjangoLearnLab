from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm, BookForm, ExampleForm

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """
    Secure book creation view.
    - Uses Django ModelForm for input validation and sanitization.
    - No raw SQL; uses ORM for safe database interaction.
    - CSRF protection is enforced in the template.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    Secure book editing view.
    - Uses Django ModelForm for input validation and sanitization.
    - No raw SQL; uses ORM for safe database interaction.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    Secure book deletion view.
    - Uses ORM for safe deletion.
    - No raw SQL.
    - Confirmation template is shown to prevent accidental deletion.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_confirm.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    """
    Secure book detail view.
    - Uses ORM for data retrieval.
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure book listing and search view.
    - Uses Django Form for validated search input.
    - No raw SQL; uses ORM query filtering.
    - Prevents SQL injection by parameterizing queries.
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            books = books.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})