from rest_framework.serializers import ModelSerializer

from posts.models import Post, Blog


class BlogListSerializer(ModelSerializer):

    class Meta:

        model = Blog
        fields = ['id', 'owner', 'name', 'description']

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = ['id', 'title', 'image', 'introduction', 'publication_date']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = '__all__'


class NewPostSerializer(ModelSerializer):
    class Meta:
        model = Post

        fields = '__all__'
        exclude = ['owner']