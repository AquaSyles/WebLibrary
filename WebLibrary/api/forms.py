from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'cover', 'language', 'stock']

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if self.instance.pk:
            if Book.objects.filter(isbn=isbn).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("A book with this ISBN already exists.")
        else:
            if Book.objects.filter(isbn=isbn).exists():
                raise forms.ValidationError("A book with this ISBN already exists.")
        return isbn