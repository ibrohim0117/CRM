from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from order.permissions import IsOrderOwnerAuthenticatedOrReadOnly
from payment.models import PaymentModel
from payment.serializers import PaymentSerializers


class PaymentListCreateAPIView(ListCreateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializers
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        # Foydalanuvchi (customer) ID sini olish
        customer_id = self.request.user.id
        print(customer_id)
        return PaymentModel.objects.filter(client__customer_id=customer_id)


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializers
    permission_classes = (IsOrderOwnerAuthenticatedOrReadOnly, )