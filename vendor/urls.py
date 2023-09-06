from django.urls import path
from .views import vendor_detail,vendor_list,add_vendor,edit_vendor


urlpatterns = [
    path('vendor/list', vendor_list, name='vendor_list'),
    path('vendor/detail', vendor_detail, name='vendor_detail'),
    path('vendor/add', add_vendor, name='add_vendor'),
    path('vendor/edit',edit_vendor, name='edit_vendor'),
]