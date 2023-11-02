from django.contrib import admin
from .models import Account, Order, Payment


admin.site.register(Account)
admin.site.register(Order)
admin.site.register(Payment)