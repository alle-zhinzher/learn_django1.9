from django.urls import path
from .views import comment_thread, comment_delete

urlpatterns = [
    path('/<int:abc>/', comment_thread, name='comment-thread'),
    path('post/<int:id>/delete/', comment_delete, name='comment-delete'),
]