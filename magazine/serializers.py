from rest_framework import serializers

from magazine.models import MagazineModel


class MagazineCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MagazineModel
        fields = ('name', )


class MagazineListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MagazineModel
        fields = '__all__'