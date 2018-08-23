from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostListSerializer


class PostListAPI(APIView):
    def get(self, request):
        """
        Devuelve la lista de anuncios
        :param request: objeto HttpRequest
        :return: objeto Response con resultado
        """
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)