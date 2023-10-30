from django.urls import path

from user.views import UserListApiView, MerchantListApiView

urlpatterns = [
    path('user/', UserListApiView.as_view()),
    path('merchant/', MerchantListApiView.as_view()),
]