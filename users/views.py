from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

# Create your views here.

def login(request):

    """
    Muestra el formulario login y procesa el login de un usuario
    :param request: objeto Httpresponse
    :return: objeto HttpResponse con el formulario renderizado
    """


    #si la peticion  es Post entonces tenemos que hacer el login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        #comprobamos las credenciales del usuario
        if user is None:
            messages.error(request, 'Usuario o contraseña incorrecto')
        else:
            # hacemos login del usuario
            django_login(request, user)
            return redirect('home')

    return render(request, 'users/login.html')


def logout(request):
    """
    Hacer el logout del usuario y redirigirlo al login
    :param request:objeto HttpRequest
    :return: objeto HttpResponse con redireccion a login
    """
    django_logout(request)
    return redirect('login')