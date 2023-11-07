from django.urls import path

from app.views import (
                       UserListCreateAPIView,
                       ClientListCreateAPIView,
                       MagazineListCreateAPIView,
                       OrderListCreateAPIView,
                       PaymentListCreateAPIView
                       )

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('client/', ClientListCreateAPIView.as_view()),
    path('magazine/', MagazineListCreateAPIView.as_view()),
    path('order/', OrderListCreateAPIView.as_view()),
    path('payment/', PaymentListCreateAPIView.as_view()),
]