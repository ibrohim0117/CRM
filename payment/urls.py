from django.urls import path
from payment.views import PaymentListCreateAPIView

urlpatterns = [
    path('payment/', PaymentListCreateAPIView.as_view()),
]