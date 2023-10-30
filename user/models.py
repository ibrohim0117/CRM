from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class Merchant(models.Model):
    status = (
        ('DEBTOR', 'DEBTOR'),
        ('PAID', 'PAID')
    )
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=255, unique=True)
    phone_num2 = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField()
    merchant_status = models.CharField(max_length=255, choices=status)

    def __str__(self):
        return self.full_name


class User(models.Model):
    status = (
        ('DEBTOR', 'DEBTOR'),
        ('PAID', 'PAID')
    )

    amount = (
        ('KG', "KG"),
        ('L', 'L'),
        ('D', 'D')
        )

    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=255, unique=True)
    phone_num2 = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10000000, decimal_places=5)
    quantity = models.DecimalField(max_digits=10000, decimal_places=5)
    quantity_type = models.CharField(max_length=255, choices=amount)
    user_status = models.CharField(max_length=255, choices=status)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name}"
