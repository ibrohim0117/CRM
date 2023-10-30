from rest_framework import serializers

from user.models import User, Merchant


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MerchantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'