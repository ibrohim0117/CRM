from rest_framework.generics import ListCreateAPIView

from order.models import OrderModel
from order.serializers import OrderSerializers


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
