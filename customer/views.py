from rest_framework import permissions, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import (
                                CustomUser,
                                ClientModel
                            )
from customer.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrSuperuserOrAuthenticatedOrReadOnly
from customer.serializers import (
    UserSerializers,
    GetMeModelSerializers,
    ClientCreatSerializers,
    ClientListSerializers,
    CustomerUpdateSerializer,
    # CustomPasswordChangeSerializer,
)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
    permission_classes = (permissions.IsAuthenticated, )



