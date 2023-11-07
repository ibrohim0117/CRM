from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Account, Payment, Order


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, attrs):
        full_name = attrs.get('full_name')
        phone_number = attrs.get('phone_number')
        # print(full_name)
        if not full_name.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Foydalanuvching ism familyasi faqat harflardan iborat bo'lishi kerak"

                 }
            )

        if Account.objects.filter(phone_number=phone_number).first():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Bu raqam bilan avval ro'yxatdan o'tilgan yangi raqam kiriting!"
                }
            )

        return attrs


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'   # noqa