from django.db import models
from common.models import cust,seller
from reseller.models import product

# Create your models here.
class cart(models.Model):
    customer = models.ForeignKey(cust,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)

    class Meta:
        db_table='cart'