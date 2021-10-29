from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Products(models.Model):
    product_name =models.CharField(max_length=15,null=True,blank=True)
    prices=models.IntegerField(null=True,blank=True)
    color=models.CharField(max_length=16,null=True,blank=True)
    size =models.CharField(max_length=10,null=True,blank=True)
    quantity=models.CharField(max_length=8,null=True,blank=True)
    


class Category(models.Model):
    category_name=models.CharField(max_length=16)
    category_description=models.TextField()


class Image(models.Model):
    image_name=models.CharField(max_length=16)
    image_id=models.CharField(max_length=8)