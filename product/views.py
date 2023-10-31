from django.shortcuts import render
from rest_framework.generics import ListAPIView

from product.models import Product, Quantity
from product.serializers import ProductListSerializer, QuantityListSerializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (permissions.AllowAny, )


class QuantityListApiView(ListAPIView):
    queryset = Quantity.objects.all()
    serializer_class = QuantityListSerializer
    # permission_classes = (permissions.AllowAny, )
