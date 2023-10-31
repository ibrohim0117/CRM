from django.urls import path

from product.views import ProductListApiView, QuantityListApiView

urlpatterns = [
    path('product/', ProductListApiView.as_view()),
    path('quantity/', QuantityListApiView.as_view()),
]