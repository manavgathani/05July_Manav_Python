from django.db import models
from datetime import datetime

# Create your models here.
class Product_mst(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.productname
    
class Product_sub_cat(models.Model):
    productprice = models.IntegerField()
    productmodal = models.CharField(max_length=20)
    productimage = models.ImageField(upload_to="images", max_length=100)
    productram = models.IntegerField()
    product = models.ForeignKey("Product_mst", on_delete=models.CASCADE)
    
    @property
    def name(self):
        return self.product.productname
    
class Product_manager(models.Model):
    creded = models.DateTimeField(default=datetime.now(), blank=True)
    fullname = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    
    