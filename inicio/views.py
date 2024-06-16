from django.shortcuts import render,redirect
from inicio.models import Vehiculo,Moto,Auto,Camion,Camioneta
from django.core.exceptions import ValidationError
from .forms import FormularioAuto, FormularioMoto, FormularioCamion, FormularioCamioneta,BuscarVehiculoForm
from django.shortcuts import render, redirect
from django.http import Http404


#vista

def inicio(request):
    return render(request, 'inicio/index.html')

def about_me(request):
    return render(request, 'about_us.html')


# Vista para seleccionar el tipo de vehículo a crear
def seleccionar_tipo_vehiculo(request):
    return render(request, 'inicio/templatesCreacion/creacion_v2.html')

# Vista general para crear vehículos
def crear_vehiculo(request, formulario_class, template_name):
    if request.method == 'POST':
        formulario = formulario_class(request.POST)
        if formulario.is_valid():
            datos_vehiculo = formulario.cleaned_data
            modelo = formulario_class.Meta.model
            if modelo.objects.filter(marca=datos_vehiculo.get('marca'), modelo=datos_vehiculo.get('modelo')).exists():
                return render(request, 'inicio/templates-resultadosVehiculos/vehiculo_ya_existe.html')
            else:
                try:
                    vehiculo = formulario.save(commit=False)
                    vehiculo.full_clean()  # Ejecuta las validaciones del modelo
                    vehiculo.save()
                    return redirect('creacion_exitosa', vehiculo.id, modelo.__name__.lower())
                except ValidationError as e:
                    formulario.add_error(None, e.message)  # Añadir error no relacionado a un campo específico
        # Si el formulario no es válido, renderiza el formulario con los errores
        return render(request, template_name, {'formulario': formulario})
    else:
        formulario = formulario_class()
    return render(request, template_name, {'formulario': formulario})

# Vistas específicas para cada tipo de vehículo
def crear_auto(request):
    return crear_vehiculo(request, FormularioAuto, 'inicio/templatesVehiculos/crear_auto.html')

def crear_moto(request):
    return crear_vehiculo(request, FormularioMoto, 'inicio/templatesVehiculos/crear_moto.html')

def crear_camion(request):
    return crear_vehiculo(request, FormularioCamion, 'inicio/templatesVehiculos/crear_camion.html')

def crear_camioneta(request):
    return crear_vehiculo(request, FormularioCamioneta, 'inicio/templatesVehiculos/crear_camioneta.html')

def creacion_exitosa(request, vehiculo_id, tipo):
    try:
        if tipo == 'auto':
            vehiculo = Auto.objects.get(id=vehiculo_id)
        elif tipo == 'moto':
            vehiculo = Moto.objects.get(id=vehiculo_id)
        elif tipo == 'camion':
            vehiculo = Camion.objects.get(id=vehiculo_id)
        elif tipo == 'camioneta':
            vehiculo = Camioneta.objects.get(id=vehiculo_id)
        else:
            return render(request, 'inicio/templates-ResultadosVehiculo/error.html', {'mensaje': 'Tipo de vehículo no válido.'})

        return render(request, 'inicio/templatesCreacion/creacion_exitosa.html', {'vehiculo': vehiculo, 'tipo': tipo})
    except (Auto.DoesNotExist, Moto.DoesNotExist, Camion.DoesNotExist, Camioneta.DoesNotExist):
        raise Http404("El vehículo solicitado no existe en la base de datos.")

def catalogo_vehiculos(request):
    autos = Auto.objects.all()
    motos = Moto.objects.all()
    camiones = Camion.objects.all()
    camionetas = Camioneta.objects.all()
    return render(request, 'inicio/templatesCreacion/catalogo_vehiculos.html', {
        'autos': autos,
        'motos': motos,
        'camiones': camiones,
        'camionetas': camionetas
    })




def buscar_vehiculo(request):
    form = BuscarVehiculoForm(request.GET or None)
    vehiculos_encontrados = []

    if request.method == 'GET' and form.is_valid():
        # Obtener los datos del formulario
        marca = form.cleaned_data.get('marca')
        modelo = form.cleaned_data.get('modelo')
        combustible = form.cleaned_data.get('combustible')
        ano_fabricacion = form.cleaned_data.get('ano_fabricacion')

        # Crear un diccionario de filtros
        filtros = {}

        # Agregar filtros si los campos están completos
        if marca:
            filtros['marca__icontains'] = marca
        if modelo:
            filtros['modelo__icontains'] = modelo
        if combustible:
            filtros['combustible__icontains'] = combustible
        if ano_fabricacion:
            filtros['ano_fabricacion'] = ano_fabricacion

        # Filtrar sobre las subclases concretas solo si hay filtros aplicados
        if filtros:
            autos = Auto.objects.filter(**filtros)
            motos = Moto.objects.filter(**filtros)
            camiones = Camion.objects.filter(**filtros)
            camionetas = Camioneta.objects.filter(**filtros)

            vehiculos_encontrados = list(autos) + list(motos) + list(camiones) + list(camionetas)

    return render(request, 'inicio/templates-resultadosVehiculos/resultado_busqueda_vehiculo.html', {'form': form, 'vehiculos_encontrados': vehiculos_encontrados})


def eliminar_auto(request):
    if request.method == 'POST':
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        
        # Mensajes de depuración
        print(f"Marca recibida: {marca}")
        print(f"Modelo recibido: {modelo}")
        
        try:
            vehiculo = Vehiculo.objects.get(marca__iexact=marca, modelo__iexact=modelo)
            print(f"Vehículo encontrado: {vehiculo}")
            vehiculo.delete()
            return redirect('catalogo_vehiculos_logged')
        except Vehiculo.DoesNotExist:
            print("Vehículo no encontrado")
            return render(request, 'inicio/resultado_busqueda_vehiculo.html', {'error': 'Vehículo no encontrado'})

    return redirect('catalogo_vehiculos_logged')