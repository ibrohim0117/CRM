from django.urls import path

from app.views import (
    UserListCreateAPIView,
    ClientListCreateAPIView,
    MagazineListCreateAPIView,
    OrderListCreateAPIView,
    PaymentListCreateAPIView,
    GetMeUserApiView,
)

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)


urlpatterns = [
    path('user/', UserListCreateAPIView.as_view(), name='user'),
    path('client/', ClientListCreateAPIView.as_view()),
    path('magazine/', MagazineListCreateAPIView.as_view()),
    path('order/', OrderListCreateAPIView.as_view()),
    path('payment/', PaymentListCreateAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-me', GetMeUserApiView.as_view(), name='get_me'),
]