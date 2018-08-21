from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from posts.forms import PostForm
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

def post_detail(request, pk):
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



def create_post(request):
    """
    Muestra el formulario para crear un post y lo procesa
    :param request: objeto HttpRequest
    :return: HttpResponse con la respuesta
    """
    # si la peticion es post, entonces tenemos que crear el post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # creamos el post
            post = form.save()
            # limpiar el formulario
            form = PostForm()
            # Devolvemos un mensaje de OK
            messages.success(request, 'Anuncio creado correctamente')
    else:
        # si no es post, tenemos que mostrar un formulario vacío
        form = PostForm()
    context = {'form': form}
    return render(request, 'posts/form.html', context)