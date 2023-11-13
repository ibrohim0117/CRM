from django.db import models

from customer.models import CustomUser


class MagazineModel(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} --> {self.owner.full_name}"