from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    name = request.GET.get('name', 'Unknown')
    message = 'Hello {0}'.format(name)
    return HttpResponse(message)