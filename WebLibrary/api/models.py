from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    language = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return self.title

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_date = models.DateField()
    return_date = models.DateField()
    customer_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.book.title} rented by {self.customer_name}"