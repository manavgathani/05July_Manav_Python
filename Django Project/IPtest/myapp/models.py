from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address= models.TextField()