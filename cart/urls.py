from django.urls import path
from .views import cart_list,cart_detail,upload_cart,edit_cart


urlpatterns = [
    path("detail/<int:id>/", cart_detail, name="cart_detail"),
    path("edit/<int:id>/", edit_cart, name="edit_cart"),
    path("list/", cart_list, name="cart_list"),
    path("upload/",upload_cart, name="upload_cart")
]