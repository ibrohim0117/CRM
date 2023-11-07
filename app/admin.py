from django.contrib import admin
from .models import (
    UserModel,
    ClientModel,
    MagazineModel,
    OrderModel,
    PaymentModel
)


admin.site.register(UserModel)
admin.site.register(ClientModel)
admin.site.register(MagazineModel)
admin.site.register(OrderModel)
admin.site.register(PaymentModel)