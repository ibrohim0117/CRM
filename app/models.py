from django.db import models


class UserModel(models.Model):
    ROLE = (
        (0, 'Superuser'),
        (1, 'Admin'),
        (2, 'Customer')
    )

    STATUS = (
        (0, 'Debtor'),
        (1, 'Paid'),
    )

    status = models.IntegerField(choices=STATUS)
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=13, unique=True)

    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class ClientModel(models.Model):
    STATUS = (
        (0, 'Debtor'),
        (1, 'Paid'),
        (3, 'Pending')
    )

    status = models.IntegerField(choices=STATUS)
    full_name = models.CharField(max_length=120)
    phone_number1 = models.CharField(max_length=13, unique=True)
    phone_number2 = models.CharField(max_length=13, blank=True, null=True)
    debt_amount = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class MagazineModel(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} --> {self.owner.full_name}"


class OrderModel(models.Model):
    client = models.ForeignKey(UserModel, models.CASCADE)
    magazine = models.ForeignKey(MagazineModel, models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    expire_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} --> {self.client.full_name} --> {self.magazine.name}"


class PaymentModel(models.Model):
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    magazine = models.ForeignKey(MagazineModel, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.full_name} --> {self.amount}"

