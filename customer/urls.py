from django.urls import path

from .views import (
    UserListCreateAPIView,
    GetMeUserApiView,
    ClientListCreateAPIView,
    CustomerRetrieveUpdateDestroyAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ClientOrdersListView,
    ClientPaymentList,
)

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)


urlpatterns = [
    path('customer/', UserListCreateAPIView.as_view(), name='user'),
    # path('change/', CustomChangePasswordView.as_view(), name='user'),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-me', GetMeUserApiView.as_view(), name='get_me'),
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view()),
    path('client/order_list/<int:pk>/', ClientOrdersListView.as_view()),
    path('client/payment_list/<int:pk>/', ClientPaymentList.as_view()),
]