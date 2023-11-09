from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from app.models import UserModel, ClientModel, MagazineModel, OrderModel, PaymentModel


class UserSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, max_length=255)

    class Meta:
        model = UserModel
        fields = ['status', 'user', 'full_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        full_name = attrs.get('full_name')
        phone_number = attrs.get('phone_number')
        confirm_password = (attrs.get('confirm_password'))
        password = (attrs.get('password'))
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

        if confirm_password == password:
            attrs.pop('confirm_password')
        else:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Invalid password"
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


class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        phone_number = obj['phone_number']
        tokens = UserModel.objects.get(phone_number=phone_number).tokens
        return tokens

    class Meta:
        model = UserModel
        fields = ('phone_number', 'tokens', 'password')

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        # user = authenticate(phone_number=phone_number, password=password)
        # if not user:
        #     raise AuthenticationFailed({
        #         'message': 'phone_number or password is not correct'
        #     })

        data = {
            'phone_number': phone_number,
        }
        return data