from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Router for API endpoints
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # Token authentication endpoint.
    # Accepts POST requests with username & password, returns an authentication token.
    path('auth-token/', obtain_auth_token, name='auth-token'),
    path('', include(router.urls)),
]