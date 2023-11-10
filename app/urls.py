from django.urls import path

from app.views import (
    UserListCreateAPIView,
    ClientListCreateAPIView,
    MagazineListCreateAPIView,
    OrderListCreateAPIView,
    PaymentListCreateAPIView,
    UserLoginView,
    TokenRefreshCustomView,
)


urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('client/', ClientListCreateAPIView.as_view()),
    path('magazine/', MagazineListCreateAPIView.as_view()),
    path('order/', OrderListCreateAPIView.as_view()),
    path('payment/', PaymentListCreateAPIView.as_view()),
    path('signin/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshCustomView.as_view(), name='token_refresh'),
]