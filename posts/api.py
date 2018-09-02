from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Blog
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer, BlogListSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['owner__username']
    ordering_fields = ['name']


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'full_text']
    ordering_fields = ['title', 'publication_date']
    ordering = ['-publication_date']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def get_queryset(self):
        username = self.request.user.username
        return Post.objects.filter(blog__owner=username)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    #Api para detalle, actualizacion y eliminacion de anuncio

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [PostPermissions]


class MyPostsAPI(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)