from rest_framework.generics import ListAPIView, RetrieveAPIView
from post.models import Post
from post.api.serializers import (PostSerializer, PostDetailSerializer)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
