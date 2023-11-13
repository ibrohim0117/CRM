from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from magazine.models import MagazineModel
from magazine.serializers import MagazineCreateSerializers, MagazineListSerializers


class MagazineListCreateAPIView(ListCreateAPIView):
    queryset = MagazineModel.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MagazineCreateSerializers

        elif self.request.method == 'GET':
            return MagazineListSerializers

    # faqt o'zi qo'shgan magazinlar ro'yxatini oladi
    def get_queryset(self):
        user = self.request.user
        return MagazineModel.objects.filter(owner=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
