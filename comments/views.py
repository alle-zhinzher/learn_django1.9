from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponse
from django.contrib import messages

from .models import Comment
from .forms import CommentForm


def comment_delete(request, id=None):
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404
    if obj.user != request.user:
        reponse = HttpResponse('You have not premision to do this')
        reponse.status_code = 403
        return reponse

    if request.method == 'POST':
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, 'Comment has been deleted')
        return HttpResponseRedirect(parent_obj_url)
    return render(request, 'confirm_delete.html', context={
                                            'object': obj,
                                        })


def comment_thread(request, id=None):
    try:
        obj = Comment.objects.get(id=id)
    except:
        raise Http404
    if not obj.is_parent:
        obj = obj.parent
    initial_data = {
        'content_type': obj.content_type,
        'object_id': obj.object_id,
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
        return HttpResponseRedirect(obj.get_absolute_url())

    return render(request, 'comment_thread.html', {
                                                'comment': obj,
                                                'form': form,
    })
