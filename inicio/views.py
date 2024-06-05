from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
import random
from inicio.models import Vehiculo

# Create your views here.
#vista
def inicio(request):
    #return HttpResponse('Hola mundo')
    return render(request, 'inicio/index.html')
# Create your views here.

def template1(request,nombre,apellido):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi template 1</h1> -- Fecha: {fecha} Hola {nombre} {apellido}')

# <h1> titulo mayor grado <h1> // <h6> titulo menor grado <h6>

def template2(request,nombre,apellido):
    
    archivo_abierto = open(r'C:\Users\Win10\Desktop\Inicio DJANGO\templates\template2.html')
    
    template =  Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    
    datos = {
        'fecha' : datetime.now(),
        'nombre' : nombre,
        'apellido' : apellido
    }
    
    contexto = Context(datos)
    template_renderizado = template.render(contexto)
    
    
    return HttpResponse(template_renderizado)

def template3(request,nombre,apellido):
        
    template = loader.get_template('template3.html')
    
    fecha = datetime.now()
    
    datos = {
        'fecha' : datetime.now(),
        'nombre' : nombre,
        'apellido' : apellido
    }
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def template4(request, nombre, apellido):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        }
    
    return render(request,'template4.html', datos)

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_Vehiculo(request):
    auto2 = Vehiculo (marca = 'Fiat', modelo = 'Siena')
    auto2.save()
    return render(request , 'inicio/index.html', {'auto2' : auto2})