from django.urls import path
from .views import review_detail,review_list,add_review,review_update


urlpatterns = [
    path('list', review_list, name='review_list'),
    path('detail/<int:id>/', review_detail, name='review_detail'),
    path('add', add_review, name='add_review'),
    path('update/<int:id>/', review_update, name='review_update'),
]