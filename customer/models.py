from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    STATUS_CHOICES = (
        (0, 'Debtor'),
        (1, 'Paid'),
        (2, 'Pending')
    )
    full_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.full_name} --> {self.phone_number}"


class ClientModel(models.Model):
    STATUS_CHOICES = (
        (0, 'Debtor'),
        (1, 'Paid'),
        (2, 'Pending')
    )

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    full_name = models.CharField(max_length=120)
    phone_number1 = models.CharField(max_length=13, unique=True)
    phone_number2 = models.CharField(max_length=13, blank=True, null=True)
    debt_amount = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name





