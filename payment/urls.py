from django.urls import path
from payment.views import PaymentListCreateAPIView, PaymentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('payment/', PaymentListCreateAPIView.as_view()),
    path('payment/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view())
]