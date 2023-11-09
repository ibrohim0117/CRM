from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.response import Response

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
                             LoginSerializer
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


class LoginView(GenericAPIView):
    # http://127.0.0.1:8000/user/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)



