from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class Merchant(models.Model):
    status = (
        (0, 'DEBTOR'),
        (1, 'PAID')
    )
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=255, unique=True)
    phone_num2 = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField()
    merchant_status = models.IntegerField(choices=status)

    def __str__(self):
        return self.full_name


class User(models.Model):
    status = (
        (0, 'DEBTOR'),
        (1, 'PAID')
    )
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num1 = models.CharField(max_length=255, unique=True)
    phone_num2 = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField()
    user_status = models.IntegerField(choices=status)

    def __str__(self):
        return f"{self.full_name}"