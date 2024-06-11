from django.shortcuts import render
import random
from inicio.models import Vehiculo

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
        
        if marca and modelo:  # Verifica que se hayan proporcionado valores para la marca y el modelo
            if Vehiculo.objects.filter(marca=marca, modelo=modelo).exists():
                # Si el vehículo ya existe en la base de datos, redirige a una página de error
                return render(request, 'inicio/vehiculo_ya_existe.html')
            else:
                # Si el vehículo no existe, créalo y redirige a la página de éxito
                auto = Vehiculo(marca=marca, modelo=modelo)
                auto.save()
                return render(request, 'inicio/creacion_exitosa.html', {'vehiculo': auto})
        else:
            # Si falta algún dato, muestra un mensaje de error o redirige a otra página
            return render(request, 'inicio/error.html')
    else:
        # Si la solicitud no es POST, simplemente renderiza la página de creación
        return render(request, 'inicio/creacion_v2.html')
