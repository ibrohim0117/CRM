from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from app.models import Account, Order, Payment
from app.serializers import AccountSerializers, OrderSerializers, PaymentSerializers


class AccountListView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers


class PaymentListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = PaymentSerializers


class OrderListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = OrderSerializers


class AccountCreatView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
