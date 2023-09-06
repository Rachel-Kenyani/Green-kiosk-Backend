from django.db import models
from inventory.models import Product
from cart.models import ShoppingCart
from customer.models import Customer
from discounts.models import Discount
from payments.models import Payment

class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    carts = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='carts')
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders_related_to_customer')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='orders')
    location = models.CharField(max_length=32)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return f"Order {self.pk}"




