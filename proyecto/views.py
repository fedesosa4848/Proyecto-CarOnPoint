from django.http import HttpResponse

# Create your views here.
#vista
def inicio(request):
    return HttpResponse('Hola mundo')