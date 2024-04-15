from django.db import models

# Create your models here.
class students(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True , blank=True)
    addresh=models.TextField(null=True , blank=True)
 
    

class nm(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    #it is for printing object value in shell command
    def __str__(self) -> str:
        return self.name 