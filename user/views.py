from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView

from user.models import User, Merchant
from user.serializers import UserListSerializer, MerchantListSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # permission_classes = (permissions.AllowAny, )


class MerchantListApiView(ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantListSerializer
    # permission_classes = (permissions.AllowAny, )
