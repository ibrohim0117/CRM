from rest_framework import permissions, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import (
                                CustomUser,
                                MagazineModel,
                                ClientModel
                            )
from customer.permissions import IsAuthenticatedOrReadOnly
from customer.serializers import (
                                 UserSerializers,
                                 GetMeModelSerializers,
                                 MagazineSerializers,
                                 ClientSerializers
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


class GetMeUserApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeModelSerializers(user).data
        print(serializer_data)
        return Response(serializer_data)


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializers
    permission_classes = (permissions.IsAuthenticated, )


class MagazineListCreateAPIView(ListCreateAPIView):
    queryset = MagazineModel.objects.all()
    serializer_class = MagazineSerializers
    permission_classes = (permissions.IsAuthenticated, )
