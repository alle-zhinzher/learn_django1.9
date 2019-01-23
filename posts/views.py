from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'list'
    }
    return render(request, 'index.html', context=context)


def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, 'post_form.html', context={'form': form})


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', context={'post': instance})


def post_update(request):
    context = {
        'title': 'update'
    }
    return render(request, 'index.html', context=context)


def post_delete(request):
    context = {
        'title': 'list'
    }
    return render(request, 'index.html', context=context)
