from rest_framework.serializers import Serializer

from user.models import User


class UserSignUpSerializer(Serializer):  # noqa
    class Meta:
        model = User
        fields = '__all__'
