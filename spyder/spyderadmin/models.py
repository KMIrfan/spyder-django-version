from django.db import models

# Create your models here.
class spyderadmin(models.Model):
    user_name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    class Meta:
        db_table = 'spyderadmin'