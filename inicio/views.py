from django.shortcuts import render
import random
from inicio.models import Vehiculo
from django.core.exceptions import ValidationError


#vista
def inicio(request):
    return render(request, 'inicio/index.html')


def probando(request):

    return render(request, 'probando_if_for.html')

def crear_Vehiculo(request,marca,modelo):
    auto2 = Vehiculo (marca = marca, modelo = modelo)
    auto2.save()
    return render(request , 'Vehiculos-templates/creacion.html', {'auto2' : auto2})


def crear_auto_v2(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        combustible = request.POST.get('combustible')
        ano_fabricacion = request.POST.get('ano_fabricacion')

        
        if marca and modelo:  # Verifica que se hayan proporcionado valores para la marca y el modelo
            if Vehiculo.objects.filter(marca=marca, modelo=modelo).exists():
                # Si el vehículo ya existe en la base de datos, redirige a una página de error
                return render(request, 'inicio/vehiculo_ya_existe.html')
            else:               
                try:
                    auto = Vehiculo(marca=marca, modelo=modelo, combustible=combustible, ano_fabricacion=ano_fabricacion)
                    auto.clean()  # Esto activará la validación definida en el modelo
                    auto.save()
                    return render(request, 'inicio/creacion_exitosa.html', {'auto': auto})
                except ValidationError as e:
                    error_message = e.message
                    return render(request, 'inicio/error.html', {'error_message': error_message})
    else:
        # Si la solicitud no es POST, simplemente renderiza la página de creación
        return render(request, 'inicio/creacion_v2.html')
    
def catalogo_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'inicio/catalogo_vehiculos.html', {'vehiculos': vehiculos})
