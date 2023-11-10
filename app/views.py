from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.models import (
                        CustomUser,
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


class UserLoginView(TokenObtainPairView):
    serializer_class = UserSerializers


class TokenRefreshCustomView(TokenRefreshView):
    serializer_class = UserSerializers


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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