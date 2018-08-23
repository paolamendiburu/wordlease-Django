from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [PostPermissions]

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

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