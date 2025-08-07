from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

    # Using DjangoFilterBackend, filters.SearchFilter, and filters.OrderingFilter for advanced querying
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'id']  # Allow ordering by these fields
    ordering = ['id']  # Default ordering

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required