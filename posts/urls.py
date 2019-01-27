from django.urls import path
from .views import (post_create,
                    post_delete, post_detail,
                    post_list, post_update)

urlpatterns = [
    path('', post_list, name='post-list'),
    path('create/', post_create),
    path('post/<int:id>/edit/', post_update, name='post-detail'),
    path('post/<int:id>/', post_detail, name='post-detail'),
    path('post/<int:id>/delete/', post_delete, name='list-delete'),
]
