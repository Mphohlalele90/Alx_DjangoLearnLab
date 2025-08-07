from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

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

# ---------------------------------------------------------
# TESTS (for demo/learning only; move to test_views.py in real code)
# ---------------------------------------------------------
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a book for detail/update/delete tests
        self.book = Book.objects.create(
            title='Sample Book',
            author='Author Name',
            publication_year=2022
        )

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)

    def test_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Sample Book')

    def test_create_book_requires_auth(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': 'Another Author', 'publication_year': 2023}
        response = self.client.post(url, data)
        self.assertIn(response.status_code, [401, 403])  # Not authenticated

        # Now authenticate and try again
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_requires_auth(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Title', 'author': 'Author Name', 'publication_year': 2022}
        response = self.client.put(url, data)
        self.assertIn(response.status_code, [401, 403])  # Not authenticated

        self.client.login(username='testuser', password='testpass')
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book_requires_auth(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403])  # Not authenticated

        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_search_books(self):
        url = reverse('book-list') + '?search=Sample'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_ordering_books(self):
        # Create another book with a different title/year
        Book.objects.create(title='A Book', author='Author Name', publication_year=2020)
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        titles = [book['title'] for book in response.data]
        self.assertEqual(sorted(titles), titles)