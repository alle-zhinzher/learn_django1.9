from urllib.parse import quote_plus
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect, render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

from comments.forms import CommentForm
from comments.models import Comment
from post.forms import PostForm
from post.models import Post
from .utils import get_read_time


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


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    print(get_read_time(instance.get_markdown()),"ERGREG")
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)

    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = instance.comments
    return render(request, 'post_detail.html', context={'post': instance,
                                                        'share_string': share_string,
                                                        'comments': comments,
                                                        'comment_form': form,
                                                        })


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


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
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("post-list")
