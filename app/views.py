from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from app.models import (
                        UserModel,
                        ClientModel,
                        MagazineModel,
                        OrderModel,
                        PaymentModel
                        )
from app.serializers import (
                             UserSerializers,
                             ClientSerializers,
                             MagazineSerializers,
                             OrderSerializers,
                             PaymentSerializers
                             )


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializers


class MagazineListCreateAPIView(ListCreateAPIView):
    queryset = MagazineModel.objects.all()
    serializer_class = MagazineSerializers


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers


class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializers


