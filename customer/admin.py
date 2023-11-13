from django.contrib import admin

from customer.models import CustomUser, ClientModel

admin.site.register(CustomUser)
admin.site.register(ClientModel)

