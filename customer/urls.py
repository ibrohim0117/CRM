from django.urls import path

from .views import (
    UserListCreateAPIView,
    GetMeUserApiView,
    ClientListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
)

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)


urlpatterns = [
    path('user/', UserListCreateAPIView.as_view(), name='user'),
    path('user/up_de', UserRetrieveUpdateDestroyAPIView.as_view(), name='up_de'),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-me', GetMeUserApiView.as_view(), name='get_me'),
    path('client/', ClientListCreateAPIView.as_view()),
]