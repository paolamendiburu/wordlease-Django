from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer


class PostListAPI(ListCreateAPIView):
    #api para hacer listado de todos los anuncios y creacion de anuncio
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return NewPostSerializer if self.request.method == 'POST' else PostListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    #Api para detalle, actualizacion y eliminacion de anuncio
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

