from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from utility.validation_phone import validate_phone_number
from .models import CustomUser, ClientModel


class UserSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, max_length=255)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number', 'status', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_phone_number(self, value):
        # Telefon raqami formatini tekshirish uchun
        if not validate_phone_number(value):
            raise serializers.ValidationError("Telefon raqami faqat raqamlardan iborat bo'lishi kerak.")
        return value

    def validate_status(self, value):
        # Ma'lumot holati uchun to'g'ri qiymatlarini tekshirish
        if value not in [0, 1, 2]:
            raise serializers.ValidationError("Noto'g'ri ma'lumot holati.")
        return value

    def validate(self, attrs):
        # confirm_password va password mosligini tekshirish
        confirm_password = (attrs.get('confirm_password'))
        password = (attrs.get('password'))

        if confirm_password == password:
            attrs.pop('confirm_password')
            attrs['password'] = make_password(password)
        else:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Invalid password"
                }
            )
        # print(attrs)
        return attrs


# class CustomPasswordChangeSerializer(serializers.Serializer):   # noqa
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         print(user, 'serializer')
#         if not user.check_password(value):
#             raise serializers.ValidationError("Old password is incorrect.")
#         return value
#
#     def validate_new_password(self, value):   # noqa
#         # Iltimos, yangi parolingizni tekshirish uchun o'zingizning talablarizni qo'shing
#         # Masalan: 8 belgidan ko'p, katta va kichik harf, raqam, xususiy belgilar, kabi.
#         return value


class GetMeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'phone_number', 'status']


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ['status', 'full_name', 'phone_number1', 'phone_number2', 'debt_amount']
