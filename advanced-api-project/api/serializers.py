from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields of the Book model and adds custom validation
# to ensure the publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Custom validation: publication_year cannot be in the future.
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer serializes the Author's name and includes a nested list of books.
# The nested relationship is handled by including BookSerializer(many=True) for 'books'.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']