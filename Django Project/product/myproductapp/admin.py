from django.contrib import admin
from myproductapp import models

# Register your models here.
admin.site.register(models.Product_mst)
admin.site.register(models.Product_sub_cat)