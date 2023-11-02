from rest_framework import serializers

from app.models import Account, Payment, Order


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'