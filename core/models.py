from django.db import models
from django.db.models.fields import CharField
class Products(models.Model):
    title=models.CharField(max_length=220)
    price=models.FloatField()
    discount=models.FloatField()
    category=models.CharField(max_length=220)
    description=models.TextField()
    image=models.ImageField(max_length=350)
    # image=models.CharField(max_length=350)