from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     CreateAPIView,
                                     )
from post.api.serializers import (PostSerializer, PostDetailSerializer,
                                  PostCreateUpdateSerializer,
                                  )

from post.models import Post


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'



class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
