from django.urls import path

from magazine.views import MagazineListCreateAPIView

urlpatterns = [
    path('magazine/', MagazineListCreateAPIView.as_view()),
]

