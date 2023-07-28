from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.IntegerField()
    published_date=models.DateField()
    description=models.CharField(max_length=200)