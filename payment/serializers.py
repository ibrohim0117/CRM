from rest_framework import serializers

from payment.models import PaymentModel


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'