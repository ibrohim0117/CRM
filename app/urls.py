from django.urls import path

from app.views import (
    UserListCreateAPIView,
    ClientListCreateAPIView,
    MagazineListCreateAPIView,
    OrderListCreateAPIView,
    PaymentListCreateAPIView,
)

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)

...

urlpatterns = [
    path('user/', UserListCreateAPIView.as_view()),
    path('client/', ClientListCreateAPIView.as_view()),
    path('magazine/', MagazineListCreateAPIView.as_view()),
    path('order/', OrderListCreateAPIView.as_view()),
    path('payment/', PaymentListCreateAPIView.as_view()),
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]