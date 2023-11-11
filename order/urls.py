from django.urls import path

from order.views import OrderListCreateAPIView

urlpatterns = [
    path('order/', OrderListCreateAPIView.as_view()),
]