from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
#vista
def inicio(request):
    return HttpResponse('Hola mundo')
# Create your views here.

def template1(request,nombre,apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi template 1</h1> -- Fecha: {fecha} Hola {nombre} {apellido}')

# <h1> titulo mayor grado <h1> // <h6> titulo menor grado <h6>

def template2(request,nombre,apellido):
    
    archivo_abierto = open(r'C:\Users\Win10\Desktop\Inicio DJANGO\templates\template2.html')
    
    template =  Template(archivo_abierto.read())
    
    
    return HttpResponse('')
