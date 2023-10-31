from rest_framework import serializers

from product.models import Product, Quantity


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class QuantityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = '__all__'