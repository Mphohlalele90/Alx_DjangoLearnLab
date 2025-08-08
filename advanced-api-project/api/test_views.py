from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author  # Adjust import if Author model is elsewhere

class BookAPITests(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        # Create authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Jane Smith")
        # Book data for model creation (not API payload)
        self.book_data = {
            "title": "Sample Book",
            "author": self.author1,
            "published_date": "2021-01-01",
            "isbn": "1234567890",
            "price": "10.99"
        }
        self.book = Book.objects.create(**self.book_data)

    def authenticate(self):
        self.client.login(username='testuser', password='testpass')

    def test_create_book_authenticated(self):
        self.authenticate()
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author2.id,  # Use PK for API call
            "published_date": "2022-02-02",
            "isbn": "0987654321",
            "price": "15.99"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Unauth Book",
            "author": self.author1.id,
            "published_date": "2020-12-12",
            "isbn": "1122334455",
            "price": "20.00"
        }
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        self.authenticate()
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": self.author1.id,
            "published_date": "2021-01-01",
            "isbn": "1234567890",
            "price": "10.99"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        self.authenticate()
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_author(self):
        Book.objects.create(title="Another Book", author=self.author2, published_date="2022-05-05", isbn="2222222222", price="17.99")
        url = reverse('book-list')
        response = self.client.get(url, {"author": self.author2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data:
            self.assertEqual(item['author'], self.author2.id)

    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {"search": "Sample"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Sample" in book['title'] for book in response.data))

    def test_order_books_by_price(self):
        Book.objects.create(title="Cheap Book", author=self.author1, published_date="2022-01-01", isbn="3333333333", price="1.99")
        url = reverse('book-list')
        response = self.client.get(url, {"ordering": "price"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices = [float(book['price']) for book in response.data]
        self.assertEqual(prices, sorted(prices))

    def test_permission_enforced(self):
        # Try update without auth
        url_update = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Should Not Update",
            "author": self.author1.id,
            "published_date": "2021-01-01",
            "isbn": "1234567890",
            "price": "10.99"
        }
        response = self.client.put(url_update, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # Try delete without auth
        url_delete = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url_delete)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])