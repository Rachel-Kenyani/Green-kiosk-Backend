from django.urls import path
from .views import CustomerListView, CustomerDetailView
from .views import ProductListView, ProductDetailView
from .views import CartListView, CartDetailView
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path("customer/",CustomerListView.as_view(), name= "customer_list_view"),
    path("customer/<int:id>/",CustomerDetailView.as_view(), name= "customer_detail_view"),

    path("product/",ProductListView.as_view(), name= "product_list_view"),
    path("product/<int:id>/",ProductDetailView.as_view(), name= "product_detail_view"),

    path("cart/",CartListView.as_view(), name= "cart_list_view"),
    path("cart/<int:id>/",CartDetailView.as_view(), name= "cart_detail_view"),

    path("order/",OrderListView.as_view(), name= "cart_list_view"),
    path("order/<int:id>/",OrderDetailView.as_view(), name= "cart_detail_view"),



]