from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

# Create your views here.
from users.forms import LoginForm


def login(request):

    """
    Muestra el formulario login y procesa el login de un usuario
    :param request: objeto Httpresponse
    :return: objeto HttpResponse con el formulario renderizado
    """




    #si la peticion  es Post entonces tenemos que hacer el login
    if request.method == 'POST':
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

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    """
    Hacer el logout del usuario y redirigirlo al login
    :param request:objeto HttpRequest
    :return: objeto HttpResponse con redireccion a login
    """
    django_logout(request)
    return redirect('login')