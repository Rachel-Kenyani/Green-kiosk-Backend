from django.urls import path
from .views import order_detail,order_list,create_order,pay_order


urlpatterns = [
    path('order/list', order_list, name='order_list'),
    path('order/detail', order_detail, name='order_detail'),
    path('order/create', create_order, name='create_order'),
    path('order/pay',pay_order, name='pay_order'),
]