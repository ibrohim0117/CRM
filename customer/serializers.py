from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from utility.validation_phone import validate_phone_number
from .models import CustomUser, MagazineModel, ClientModel


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
        print(attrs)
        return attrs


class GetMeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number', 'status']


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class MagazineSerializers(serializers.ModelSerializer):
    class Meta:
        model = MagazineModel
        fields = '__all__'