from django.db import models

from customer.models import CustomUser, MagazineModel


class PaymentModel(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    magazine = models.ForeignKey(MagazineModel, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.full_name} --> {self.amount}"