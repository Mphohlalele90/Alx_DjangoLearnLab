from django.db import models

# The Author model represents an author entity with a name.
class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the author.")

    def __str__(self):
        return self.name

# The Book model represents a book with a title, publication year,
# and a foreign key to Author, creating a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the book.")
    publication_year = models.IntegerField(help_text="Year the book was published.")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, help_text="The author of the book.")

    def __str__(self):
        return self.title