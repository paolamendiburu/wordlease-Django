from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login

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

    return render(request, 'users/login.html', context)
