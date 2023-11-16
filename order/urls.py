from django.urls import path

from order.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('order/', OrderListCreateAPIView.as_view()),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view()),
]