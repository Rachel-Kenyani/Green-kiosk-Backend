from django.urls import path
from .views import discount_detail,discount_list,upload_discount,discount_update


urlpatterns = [
    path('list', discount_list, name='discount_list'),
    path('detail/<int:id>/', discount_detail, name='discount_detail'),
    path('add', upload_discount, name='upload_discount'),
    path('update/<int:id>/', discount_update, name='discount_update')
]



