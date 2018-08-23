from rest_framework.generics import ListAPIView, RetrieveAPIView



from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer


class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer



class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer