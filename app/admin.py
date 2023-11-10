from django.contrib import admin
from .models import (
    CustomUser,
    ClientModel,
    MagazineModel,
    OrderModel,
    PaymentModel
)


admin.site.register(CustomUser)
admin.site.register(ClientModel)
admin.site.register(MagazineModel)
admin.site.register(OrderModel)
admin.site.register(PaymentModel)