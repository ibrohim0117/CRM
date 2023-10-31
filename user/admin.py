from django.contrib import admin

from user.models import Merchant, User

admin.site.register(Merchant)
admin.site.register(User)