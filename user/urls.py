from django.urls import path

from user.views import CreateUserView

urlpatterns = [
    path('singup/', CreateUserView.as_view())
]