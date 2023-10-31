from django.db import models
from user.models import Merchant, User


class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10000000, decimal_places=2)


class Quantity(models.Model):
    AMOUNT = (
        (0, "KG"),
        (1, 'L'),
        (2, 'D')
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.IntegerField(choices=AMOUNT)