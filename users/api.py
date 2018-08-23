
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status

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

    def post(self, request):
        """
        Crea un musuario y devuelve la informacion del Usuario Creado
        :param request: Objeto de tipo HttpRequest
        :return: objeto de tipo HttpReponse
        """

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )


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

    def delete(self, request, pk):
        """
        Borra el usuario con ese pk
        :param request: Objeto de tipo HttpRequest
        :param pk:  pk del usuario que queremos eliminar
        :return: 204 o 404
        """
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        """
        Actualiza el usuario con ese pk
        :param request: Objeto de tipo HttpRequest
        :param pk:  pk del usuario que queremos actualizar
        :return: 202 o 402
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )


