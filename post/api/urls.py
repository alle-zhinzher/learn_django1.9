from django.urls import path
from post.api.views import (
                            PostListAPIView,
                            PostDetailView,
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    #path('create/', post_create),
    path('<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    #path('post/<str:slug>/edit/', post_update, name='post-update'),
    #path('post/<str:slug>/delete/', post_delete, name='list-delete'),
]