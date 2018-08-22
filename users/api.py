
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from rest_framework.views import APIView

from users.serializers import UserSerializer, UserListSerializer


class UsersAPI(APIView):

    def get(self, request):
        """
        Devuelve el listado de usuarios
        :param request: Objeto de tipo HttpRequest
        :return: objeto de tipo HttpReponse
        """

        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        """
        Devuelve el detalle de un usuario con pk <pk>
        :param request: Objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos devolver
        :return: objeto de tipo HttpReponse
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

