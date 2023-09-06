from django.urls import path
from .views import customer_list, customer_edit, customer_detail, upload_customer

urlpatterns = [
    path('list', customer_list, name='customer_list'),
    path('detail/<int:id>/', customer_detail, name='customer_detail'),
    path('add', upload_customer, name='upload_customer'),
    path('edit/<int:id>/', customer_edit, name='customer_edit'),
]
