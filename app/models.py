from django.db import models


class Account(models.Model):
    ROLE = (
        (0, 'Merchant'),
        (1, 'Client'),
    )
    STATUS = (
        (0, 'Debtor'),
        (1, 'Paid'),
    )
    full_name = models.CharField(max_length=221)
    role = models.IntegerField(choices=ROLE)
    bill = models.DecimalField(max_digits=1000000, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=221)
    extra_phone_number = models.CharField(max_length=221, null=True, blank=True)
    status = models.IntegerField(choices=STATUS)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    merchant = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='merchant')
    client = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='client')
    description = models.TextField()
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    expire_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Payment(models.Model):
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.full_name