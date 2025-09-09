from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

from django.urls import path
from . import views

urlpatterns = [
    # List all books (GET) - Public access
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # Retrieve single book (GET) - Public access
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # Create new book (POST) - Authenticated users only
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # Update book (PUT/PATCH) - Authenticated users only
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    
    # Delete book (DELETE) - Authenticated users only
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]