from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Add other fields as required

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False)

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=False)