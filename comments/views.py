from django.shortcuts import render, get_object_or_404

from .models import Comment


def comment_thread(request, abc):
    obj = get_object_or_404(Comment, id=abc)
    return render(request, 'comment_thread.html', {})


def comment_delete():
    pass
