# Create your models here.
from django.db import models
from customer.models import Customer

class Discount(models.Model):
    code = models.CharField(max_length=32, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    customers = models.ManyToManyField(Customer,"customers")

    def __str__(self):
        return self.code

