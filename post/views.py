from urllib.parse import quote_plus
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from post.forms import PostForm
from post.models import Post


def post_list(request):
    queryset = Post.objects.active().order_by('-timestamp')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(content__icontains=query)).distinct()
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
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")
    return render(request, 'post_form.html', context={'form': form})


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    return render(request, 'post_detail.html', context={'post': instance,
                                                        'share_string': share_string,})


def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Post not updated')
    return render(request, 'post_form.html', context={'post': instance,
                                                        'form': form})


def post_delete(request, slug=None):
    instance = get_object_or_404(Post, id=slug)
    instance.delete()
    messages.success(request, 'Post Deleted')
    return redirect('post-list')
