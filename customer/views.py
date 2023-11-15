from rest_framework import permissions, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import (
                                CustomUser,
                                ClientModel
                            )
from customer.permissions import IsAuthenticatedOrReadOnly
from customer.serializers import (
    UserSerializers,
    GetMeModelSerializers,
    ClientSerializers,
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


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticated, )


# class CustomChangePasswordView(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomPasswordChangeSerializer
#     permission_classes = [permissions.IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        print(user, 'view')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # old_password = serializer.validated_data.get('old_password')
        # new_password = serializer.validated_data.get('new_password')

        # if not user.cheak_password(old_password):
        #     msg = {
        #         "status": False,
        #         "message": 'Old password invalid!'
        #            }
        #     return Response(msg)
        # else:
        #     user.set_password(new_password)
        #     user.save()
        #     msg = {
        #         "status": True,
        #         "message": 'Password updated successfully!'
        #     }
        #     return Response(msg)


class GetMeUserApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeModelSerializers(user).data
        # print(serializer_data)
        return Response(serializer_data)


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializers
    permission_classes = (permissions.IsAuthenticated, )

    # faqt o'zi qo'shgan qarzdorlar ro'yxatini oladi
    def get_queryset(self):
        user = self.request.user
        # print(user)
        return ClientModel.objects.filter(customer=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(customer=user)






