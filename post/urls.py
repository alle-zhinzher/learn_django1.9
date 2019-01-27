from django.urls import path
from post.views import (post_create,
                        post_delete, post_detail,
                        post_list, post_update)

urlpatterns = [
    path('', post_list, name='post-list'),
    path('create/', post_create),
    path('post/<str:slug>/', post_detail, name='post-detail'),
    path('post/<str:slug>/edit/', post_update, name='post-update'),
    path('post/<str:slug>/delete/', post_delete, name='list-delete'),
]
