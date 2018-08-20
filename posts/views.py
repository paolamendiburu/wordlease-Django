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

def ad_detail(request, pk):
    """
     Muestra el detalle de un posts
     :param request objeto:HttpRequest
     :param pk es el identificador de un post
     :return HttpResponse con respuesta
     """
    #recuperar de la base de datos el post que me piden y ver que existe y si no existe devolver un 404
    try:
        post = Post.objects.select_related().get(pk=pk)
    except Post.DoesNotExit:
        return HttpResponse('No existe el post que buscas')

    #si existe el anuncio creamos el contesto
    context = {'post':post}

    # devover la respuesta utilizando una plantilla
    return render(request, 'posts/detail.html', context)
