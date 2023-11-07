from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import UserModel, ClientModel, MagazineModel, OrderModel, PaymentModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
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

        if UserModel.objects.filter(phone_number=phone_number).first():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Bu raqam bilan avval ro'yxatdan o'tilgan yangi raqam kiriting!"
                }
            )

        return attrs


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class MagazineSerializers(serializers.ModelSerializer):
    class Meta:
        model = MagazineModel
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'