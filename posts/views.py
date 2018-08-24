from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post, Blog


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


class BlogListView(ListView):

    model = Blog
    template_name = 'posts/bloglist.html'


    def get_queryset(self):
        result = super().get_queryset()
        return result.order_by('-publication_date')







class BlogPostsView(ListView):

    model = Post
    template_name = 'posts/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.kwargs.get('username')
        user = get_object_or_404(User,  Q(username=username))
        return qs.filter(owner=user.id).order_by('-publication_date')




class PostDetailView(View):
    def get(self, request, username, pk):
        """
         Muestra el detalle de un posts
         :param request objeto:HttpRequest
         :param pk es el identificador de un post
         :return HttpResponse con respuesta
         """
        #recuperar de la base de datos el post que me piden y ver que existe y si no existe devolver un 404
        try:
            post = Post.objects.select_related().get(owner__username=username, pk=pk)
        except Post.DoesNotExit:
            return HttpResponse('The post doesn\'t exists')

        #si existe el anuncio creamos el contesto
        context = {'post': post}

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
        Procesa el formulario para crear un usuario
        :param request: objeto HttpRequest
        :return: HttpResponse con la respuesta
        """

        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # creamos el post
            post = form.save()
            # limpiar el formulario
            form = PostForm()
            # Devolvemos un mensaje de OK
            messages.success(request, 'Post creado correctamente')
