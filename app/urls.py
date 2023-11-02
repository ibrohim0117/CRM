from django.urls import path

from app.views import AccountListView, OrderListView, PaymentListView

urlpatterns = [
    path('acc/', AccountListView.as_view()),
    path('payment/', PaymentListView.as_view()),
    path('order/', OrderListView.as_view()),
]