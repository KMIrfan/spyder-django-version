from django.db import models

# Create your models here.
class cust(models.Model):
   
    cust_fname=models.CharField(max_length=20)
    cust_lname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    cust_email=models.CharField(max_length=50)
    cust_phn=models.BigIntegerField()
    cust_pass=models.CharField(max_length=40)
    cust_cnfrmpass=models.CharField(max_length=40)
    house=models.CharField(max_length=40,default='select')
    post=models.CharField(max_length=40,default='select')
    landmark=models.CharField(max_length=40,default='select')
    dist=models.CharField(max_length=40,default='malappuram')
    state=models.CharField(max_length=40,default='kerala')
    pin=models.BigIntegerField(default=671631)


    class Meta:
        db_table = 'customer'


class seller(models.Model):
    seller_fname=models.CharField(max_length=20)
    seller_lname=models.CharField(max_length=20)
    seller_email=models.CharField(max_length=50)
    seller_phn=models.BigIntegerField()
    seller_pass=models.CharField(max_length=40)
    seller_usr=models.IntegerField(default=0)
    seller_bus=models.CharField(max_length=40)
    bank=models.CharField(max_length=40)
    seller_accnt=models.BigIntegerField()
    seller_image=models.ImageField(upload_to='seller/')
    status = models.CharField(max_length=20,default='pending')

    class Meta:
        db_table = 'seller'