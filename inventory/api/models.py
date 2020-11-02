from django.db import models

# Create your models here.
class Product(models.Model):
    pd_name = models.CharField(max_length=64,unique=True)
    pd_type = models.CharField(max_length=64)
    pd_cost = models.IntegerField(default=0)
    pd_count = models.IntegerField(default=0)

    def __str__(self):
        return f" name : {self.pd_name} count : {self.pd_count}"