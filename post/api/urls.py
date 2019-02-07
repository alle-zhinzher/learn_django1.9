from django.urls import path
from post.api.views import (PostListAPIView, PostDetailView,
                            PostDeleteView, PostUpdateView,
                            PostCreateAPIView,)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list-api'),
    path('create/', PostCreateAPIView.as_view(), name='post-create-api'),
    path('<str:slug>/', PostDetailView.as_view(), name='post-detail-api'),
    path('<str:slug>/edit/', PostUpdateView.as_view(), name='post-update-api'),
    path('<str:slug>/delete/', PostDeleteView.as_view(), name='list-delete-api'),
]