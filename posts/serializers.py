from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = ['id', 'title', 'introduction']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = '__all__'


class NewPostSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = '__all__'
        exclude = ['owner']