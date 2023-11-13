from django.db import models

from customer.models import ClientModel
from magazine.models import MagazineModel


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, models.CASCADE)
    magazine = models.ForeignKey(MagazineModel, models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    expire_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} --> {self.client.full_name} --> {self.magazine.name}"
