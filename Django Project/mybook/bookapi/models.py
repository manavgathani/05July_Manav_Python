from django.db import models

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=255)
    Isbn = models.CharField(max_length=255)
    Publisher = models.CharField(max_length=255)