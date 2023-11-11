from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from payment.models import PaymentModel
from payment.serializers import PaymentSerializers


class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializers
