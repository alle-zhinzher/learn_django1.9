from django.urls import path
from .views import comment_thread, comment_delete

urlpatterns = [
    path('<int:id>/', comment_thread, name='comment-thread'),
    path('<int:id>/delete/', comment_delete, name='comment-delete'),
]