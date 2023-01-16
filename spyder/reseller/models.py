from django.db import models
from common.models import seller

# Create your models here.
class product(models.Model):
    seller = models.ForeignKey(seller, on_delete=models.CASCADE)
    protitle=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    proid=models.IntegerField()
    prosubtitle=models.CharField(max_length=40)
    proimg=models.ImageField(upload_to='product/')
    price=models.IntegerField()
    prodesc=models.CharField(max_length=100)
    stock=models.IntegerField(default='1')


    class Meta:
        db_table='product'