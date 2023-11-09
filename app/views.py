from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

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
                             PaymentSerializers,
                             )


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     name = self.kwargs.get('full_name')
    #     print(name)
    #     # return qs.filter(place_id=place_id)


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




