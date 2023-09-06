from django.db import models
from vendor.models import Vendor

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    vendor = models.ManyToManyField(Vendor)

    def __str__(self):
        return self.name
