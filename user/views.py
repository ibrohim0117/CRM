from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from user.models import User
from user.serializers import UserSignUpSerializer


class CreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    # permission_classes = (permissions.AllowAny, )
