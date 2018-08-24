from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

# Create your views here.
from django.views import View

from users.forms import LoginForm, SignupForm


class LoginView(View):
    def get(self, request):

        """
        Muestra el formulario login
        :param request: objeto Httpresponse
        :return: objeto HttpResponse con el formulario renderizado
        """

        form = LoginForm()

        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):

        """
        Procesa el login de un usuario
        :param request: objeto Httpresponse
        :return: objeto HttpResponse con el formulario renderizado
        """


        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(username=username, password=password)

            #comprobamos las credenciales del usuario
            if user is None:
                messages.error(request, 'Usuario o contraseña incorrecto')
            else:
                # hacemos login del usuario
                django_login(request, user)
                return redirect('home')



        context = {'form': form}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        """
        Hacer el logout del usuario y redirigirlo al login
        :param request:objeto HttpRequest
        :return: objeto HttpResponse con redireccion a login
        """
        django_logout(request)
        return redirect('login')



def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()
            SignupForm()
            messages.success(request, 'The user has been createed succesfully')
    else:
        form = SignupForm()

    form = SignupForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)