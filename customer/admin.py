from django.contrib import admin

from customer.models import CustomUser, ClientModel, MagazineModel

admin.site.register(CustomUser)
admin.site.register(ClientModel)
admin.site.register(MagazineModel)
