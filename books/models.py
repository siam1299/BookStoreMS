from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    points = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="books/", null=True, blank=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
