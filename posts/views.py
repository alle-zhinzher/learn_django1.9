from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, render
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import PostForm
from .models import Post

def post_list(request):
    queryset = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(queryset, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    post = paginator.get_page(page)
    context = {
        'object_list': post,
        'title': 'list'
    }
    return render(request, 'posts_list.html', context=context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")
    return render(request, 'post_form.html', context={'form': form})


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', context={'post': instance})


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Post not updated')
    return render(request, 'post_update.html', context={'post': instance,
                                                        'form': form})


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Post Deleted')
    return redirect('post-list')
