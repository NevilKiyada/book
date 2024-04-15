from django.db import models

# Create your models here.
class book(models.Model):
    book_title = models.CharField(max_length=200)
    book_discussion = models.TextField()
    book_image=models.ImageField(upload_to="book_images")