from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from posts.models import Post


def home(request):
    """
    Muestra el listado de los ultimos posts
    :param request objeto:HttpRequest
    :return HttpResponse con respuesta
    """
    # recuperar los posts de la base de datos

    posts = Post.objects.all().order_by('-publication_date')

    # creamos contexto para poderselo pasar a la plantilla

    context = {'items': posts}

    # devover la respuesta utilizando una plantilla

    return render(request, 'posts/list.html', context)

