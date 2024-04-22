from django.db import models

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_description = models.TextField()
    book_image=models.ImageField(upload_to="book_images")
        