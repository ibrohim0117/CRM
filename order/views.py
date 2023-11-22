from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from customer import permissions
from order.models import OrderModel
from order.permissions import IsOrderOwnerAuthenticatedOrReadOnly
from order.serializers import OrderSerializers


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        # Foydalanuvchi (customer) ID sini olish
        customer_id = self.request.user.id
        return OrderModel.objects.filter(client__customer_id=customer_id)


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsOrderOwnerAuthenticatedOrReadOnly, )




