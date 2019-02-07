from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]