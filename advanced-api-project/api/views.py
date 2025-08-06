from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create, anyone can list
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Retrieve, update, or delete a book by ID
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can update/delete, anyone can retrieve
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # You can also add more customizations here (e.g., custom validation or filtering)