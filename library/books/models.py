from django.db import models

# Create your models here.

#Table Definition(schema)
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    pages=models.IntegerField()
    language=models.CharField(max_length=30)
    image=models.ImageField(upload_to="books")



