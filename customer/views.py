from rest_framework import permissions, status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import (
                                CustomUser,
                                ClientModel
                            )
from customer.permissions import (
    IsAuthenticatedOrReadOnly,
    IsOwnerOrSuperuserOrAuthenticatedOrReadOnly,
    IsClintOwnerAuthenticatedOrReadOnly
)
from customer.serializers import (
    CustomerCreateSerializers,
    GetMeModelSerializers,
    ClientCreatSerializers,
    ClientListSerializers,
    CustomerUpdateSerializer,
    ClintOrderListSerializer,
    CustomerListSerializers,
)
from order.models import OrderModel
from order.serializers import OrderSerializers
from payment.models import PaymentModel
from payment.serializers import PaymentSerializers


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerCreateSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerCreateSerializers
        elif self.request.method == 'GET':
            return CustomerListSerializers


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerUpdateSerializer
    permission_classes = (IsOwnerOrSuperuserOrAuthenticatedOrReadOnly, )


class GetMeUserApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeModelSerializers(user).data
        return Response(serializer_data)


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientCreatSerializers
    permission_classes = (permissions.IsAuthenticated, )

    # faqt o'zi qo'shgan qarzdorlar ro'yxatini oladi
    def get_queryset(self):
        user = self.request.user
        # print(user)
        return ClientModel.objects.filter(customer=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(customer=user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientCreatSerializers

        elif self.request.method == 'GET':
            return ClientListSerializers


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClientModel
    serializer_class = ClientCreatSerializers
    permission_classes = (IsClintOwnerAuthenticatedOrReadOnly, )


class ClientOrdersListView(RetrieveAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientListSerializers
    permission_classes = (IsClintOwnerAuthenticatedOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        # Obyekt ma'lumotlarini olish
        instance = self.get_object()

        # Clintga oid ma'lumotlar
        client_serializer = self.get_serializer(instance)
        client_data = client_serializer.data

        # Clintga oid OrderModel obyektlarini olish
        orders = OrderModel.objects.filter(client=instance)
        order_serializer = OrderSerializers(orders, many=True)
        orders_data = order_serializer.data

        data = {
            'client_info': client_data,
            'orders': orders_data
        }

        return Response(data)


class ClientPaymentList(RetrieveAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientListSerializers
    permission_classes = (IsClintOwnerAuthenticatedOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        client_serializer = self.get_serializer(instance)
        client_data = client_serializer.data

        payment = PaymentModel.objects.filter(client=instance)
        payment_serializer = PaymentSerializers(payment, many=True)
        payments_data = payment_serializer.data

        data = {
            'client_info': client_data,
            'payments': payments_data
        }

        return Response(data)



