from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post

class HomeView(ListView):

    model = Post
    template_name = 'posts/list.html'


    def get_queryset(self):
        result = super().get_queryset()
        return result.order_by('-publication_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Wordplease"
        return context

@method_decorator(login_required, name='dispatch')
class MyPostsView(ListView):
    model = Post
    template_name = 'posts/list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My posts"
        return context


class PostDeitalView(View):
    def get(self, request, pk):
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


@method_decorator(login_required, name='dispatch')
class PostFormView(View):

    def get(self, request):
        """
        Presenta el formulario
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """

        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/form.html', context)


    def post(self, request):
        """
        Procesa el formulario para crear un post
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """

        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # creamos el post
            post = form.save()
            # limpiar el formulario
            form = PostForm()
            # Devolvemos un mensaje de OK
            messages.success(request, 'Anuncio creado correctamente')
