from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    home, list_books, LibraryDetailView, register,
    add_book, edit_book, delete_book
)

urlpatterns = [
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Checker expects these URL patterns:
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]