from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank= True) 
    book_title = models.CharField(max_length=200)
    book_description = models.TextField()
    book_image=models.ImageField(upload_to="book_images")
        
