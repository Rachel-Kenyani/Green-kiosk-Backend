from django.urls import path
from .views import payment_create, payment_update,payment_detail,payment_list

urlpatterns = [
    path('payment/list', payment_list, name='payment_list'),
    path('payment/detail', payment_detail, name='payment_detail'),
    path('payment/create', payment_create, name='payment_create'),
    path('payment/update',  payment_update, name="payment_update")
]